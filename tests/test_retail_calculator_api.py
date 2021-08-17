"""
API tests
"""
import pytest

from http import HTTPStatus

from tests.test_helper import (
    create_valid_order,
    create_invalid_price_order,
    create_invalid_price_decimal_order,
    create_invalid_state_order,
    create_invalid_product_amount_order,
    create_non_existed_state_order,
    create_negative_amount_order,
    create_negative_price_order,
    create_zero_amount_order,
    create_zero_price_order,
    valid_order_mock,
)

pytestmark = pytest.mark.asyncio


async def test_create_valid_order(async_client):
    response = await create_valid_order(async_client)
    response_body = response.json()
    response_body.pop('stamp')

    assert response.status_code == HTTPStatus.CREATED
    assert response_body == valid_order_mock


async def test_create_invalid_price_order(async_client):
    response = await create_invalid_price_order(async_client)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


async def test_create_invalid_price_decimal_order(async_client):
    response = await create_invalid_price_decimal_order(async_client)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


async def test_create_invalid_product_amount_order(async_client):
    response = await create_invalid_product_amount_order(async_client)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


async def test_create_invalid_state_order(async_client):
    response = await create_invalid_state_order(async_client)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


async def test_create_non_existed_state_order(async_client):
    response = await create_non_existed_state_order(async_client)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


async def test_create_negative_amount_order(async_client):
    response = await create_negative_amount_order(async_client)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


async def test_create_negative_price_order(async_client):
    response = await create_negative_price_order(async_client)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


async def test_create_zero_amount_order(async_client):
    response = await create_zero_amount_order(async_client)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


async def test_create_zero_price_order(async_client):
    response = await create_zero_price_order(async_client)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
