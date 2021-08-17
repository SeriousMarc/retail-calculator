"""
Data Access Layer
"""
from decimal import Decimal

from sqlalchemy import select, insert, literal_column
from sqlalchemy.ext.asyncio import AsyncSession

from retail_calculator.db.models import Base, Order, Discount, Tax


class BaseRepository:
    def __init__(self, session: AsyncSession, model: Base):
        self.session = session
        self.model = model

    async def create(self, data: dict) -> dict:
        record = await self.session.execute(
            insert(self.model).values(**data).returning(literal_column('*')),
        )

        return record.first()

    async def select(self, data: dict) -> dict:
        record = await self.session.execute(
            select(self.model).values(**data).returning(literal_column('*')),
        )

        return record.first()


class OrderRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Order)


class DiscountRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Discount)

    async def get_rate(self, price: Decimal) -> dict:
        record = await self.session.execute(
            select(self.model.rate).where(
                self.model.price <= price,
            ).order_by('price').limit(1),
        )

        return record.first()


class TaxRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Tax)

    async def get_rate(self, state: str) -> dict:
        record = await self.session.execute(
            select(self.model.rate).where(
                self.model.state == state,
            ).limit(1),
        )

        return record.first()
