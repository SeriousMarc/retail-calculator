"""
Tests pre configuration
"""
import asyncio

from typing import AsyncGenerator

import pytest

from httpx import AsyncClient

from retail_calculator.app import app
from retail_calculator.db.utils import init_models, drop_models, prepare_db

BASE_URL = 'http://localhost:8000'


@pytest.fixture(scope='session')
def event_loop() -> AsyncGenerator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop


@pytest.fixture(autouse=True)
async def db_wrapper() -> AsyncGenerator:
    await drop_models()  # clean up if db is same for dev and test envs
    await init_models()
    await prepare_db()
    yield
    await drop_models()


@pytest.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        yield ac
