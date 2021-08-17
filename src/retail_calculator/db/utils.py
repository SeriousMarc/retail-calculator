"""
DB Utilities
"""
from sqlalchemy import select, insert, func
from sqlalchemy.exc import SQLAlchemyError

from retail_calculator.db import engine, Base, async_session
from retail_calculator.db.models import Discount, Tax
from retail_calculator.db.payload import discount_payload, tax_payload
from retail_calculator.config import logger


def session(f):
    async def wrapper(*args, **kwargs):
        result = None

        async with async_session() as a_session:
            try:
                result = await f(a_session, *args, **kwargs)
                await a_session.commit()
            except SQLAlchemyError:
                await a_session.rollback()

        return result
    return wrapper


async def insert_discount_records(a_session):
    for discount in discount_payload:
        await a_session.execute(insert(Discount).values(**discount))


async def insert_tax_records(a_session):
    for tax in tax_payload:
        await a_session.execute(insert(Tax).values(**tax))


@session
async def prepare_db(a_session):
    await insert_discount_records(a_session)
    await insert_tax_records(a_session)


@session
async def db_heartbeat(a_session):
    hb = (await a_session.execute(select(func.count(1).label('count')))).first()
    logger.error(f'Heartbeat: {bool(hb.count)}')


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
