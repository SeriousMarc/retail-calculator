"""
Test Utilities
"""
from httpx import AsyncClient, Response


async def create_valid_order(ac: AsyncClient) -> Response:
    return await ac.post(
        '/v1/orders',
        json={
            'product_amount': 2,
            'price_per_product': '500.01',
            'state': 'UT',
        },
    )


async def create_invalid_price_order(ac: AsyncClient) -> Response:
    return await ac.post(
        '/v1/orders',
        json={
            'product_amount': 2,
            'price_per_product': 'NZXT',
            'state': 'UT',
        },
    )


async def create_invalid_price_decimal_order(ac: AsyncClient) -> Response:
    return await ac.post(
        '/v1/orders',
        json={
            'product_amount': 7,
            'price_per_product': '500.01111111',
            'state': 'UT',
        },
    )


async def create_invalid_product_amount_order(ac: AsyncClient) -> Response:
    return await ac.post(
        '/v1/orders',
        json={
            'product_amount': 7.1,
            'price_per_product': '500.01',
            'state': 'UT',
        },
    )


async def create_invalid_state_order(ac: AsyncClient) -> Response:
    return await ac.post(
        '/v1/orders',
        json={
            'product_amount': 7,
            'price_per_product': '500.01',
            'state': 'NZXT',
        },
    )


async def create_non_existed_state_order(ac: AsyncClient) -> Response:
    return await ac.post(
        '/v1/orders',
        json={
            'product_amount': 7,
            'price_per_product': '500.01',
            'state': 'NZ',
        },
    )


async def create_negative_amount_order(ac: AsyncClient) -> Response:
    return await ac.post(
        '/v1/orders',
        json={
            'product_amount': -7,
            'price_per_product': '500.01',
            'state': 'NZ',
        },
    )


async def create_negative_price_order(ac: AsyncClient) -> Response:
    return await ac.post(
        '/v1/orders',
        json={
            'product_amount': 7,
            'price_per_product': '-500.01',
            'state': 'NZ',
        },
    )


async def create_zero_amount_order(ac: AsyncClient) -> Response:
    return await ac.post(
        '/v1/orders',
        json={
            'product_amount': 0,
            'price_per_product': '-500.01',
            'state': 'NZ',
        },
    )


async def create_zero_price_order(ac: AsyncClient) -> Response:
    return await ac.post(
        '/v1/orders',
        json={
            'product_amount': 7,
            'price_per_product': '0',
            'state': 'NZ',
        },
    )


valid_order_mock = {
    'product_amount': 2,
    'price_per_product': 500.01,
    'state': 'UT',
    'discount': 3,
    'tax': 6.85,
    'gross_price': 1000.02,
    'sale': 970.01,
    'net_price': 1036.46,
}
