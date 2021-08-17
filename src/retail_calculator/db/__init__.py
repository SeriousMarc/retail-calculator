"""
DB configuration
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import declarative_base, sessionmaker

from retail_calculator.config import DB_URI


engine: AsyncEngine = create_async_engine(DB_URI, future=True, echo=True)
async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session() as a_session:
        yield a_session
