"""
Application Routes
"""
from fastapi.routing import APIRouter
from fastapi import Depends
from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession


from retail_calculator.db import get_session
from retail_calculator.api.views import create_order_view
from retail_calculator.api.schemas import OrderInput, OrderOutput

router = APIRouter(redirect_slashes=False)
v1 = '/v1'


@router.post(f'{v1}/orders', status_code=HTTPStatus.CREATED)
async def create_order(payload: OrderInput, session: AsyncSession = Depends(get_session)) -> OrderOutput:
    return await create_order_view(payload, session)
