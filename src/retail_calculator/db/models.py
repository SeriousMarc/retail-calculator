"""
DB models
"""
from decimal import Decimal

from sqlalchemy import (
    Column,
    Numeric,
    BigInteger,
    String,
    DateTime,
    func,
)

from retail_calculator.db import Base


class Order(Base):
    __tablename__ = 'order'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    product_amount = Column(BigInteger, primary_key=True)
    price_per_product = Column(Numeric, nullable=True, default=Decimal(0))
    state = Column(String, nullable=False)
    discount = Column(Numeric, nullable=True, default=Decimal(0))
    tax = Column(Numeric, nullable=True, default=Decimal(0))
    stamp = Column(DateTime(timezone=True), server_default=func.now())


class Discount(Base):
    __tablename__ = 'discount'

    id = Column(BigInteger, primary_key=True)
    price = Column(Numeric, nullable=True, default=Decimal(0))
    rate = Column(Numeric, nullable=True, default=Decimal(0))


class Tax(Base):
    __tablename__ = 'tax'

    id = Column(BigInteger, primary_key=True)
    state = Column(String, nullable=False)
    rate = Column(Numeric, nullable=True, default=Decimal(0))
