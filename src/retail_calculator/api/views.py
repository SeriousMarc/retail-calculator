"""
View Business Logic
"""
from asyncio import gather
from decimal import Decimal, ROUND_05UP
from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from retail_calculator.db.repository import OrderRepository, DiscountRepository, TaxRepository
from retail_calculator.api.schemas import OrderInput, Order, OrderOutput
from retail_calculator.api.utils import calculate_discount, calculate_tax


async def create_order_view(payload: OrderInput, session: AsyncSession) -> OrderOutput:
    order_repo = OrderRepository(session)
    discount_repo = DiscountRepository(session)
    tax_repo = TaxRepository(session)

    gross_price = payload.product_amount * payload.price_per_product

    try:
        discount, tax = await gather(
            discount_repo.get_rate(price=gross_price),
            tax_repo.get_rate(state=payload.state),
        )

        discount_rate = getattr(discount, 'rate', Decimal('0'))

        if tax is None:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail=f'Did not find given state:"{payload.state}"',
            )

        order = Order(discount=discount_rate, tax=tax.rate, **payload.dict())
        order = await order_repo.create(order.dict())

        await session.commit()
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))

    try:
        sale = calculate_discount(gross_price, discount_rate)
        net_price = calculate_tax(sale, tax.rate)
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail=str(e))
    # TODO add pydantic validators for negative values, zero value and etc

    return OrderOutput(
        gross_price=gross_price,
        sale=sale.quantize(Decimal('.01'), rounding=ROUND_05UP),
        net_price=net_price.quantize(Decimal('.01'), rounding=ROUND_05UP),
        **order,
    )
