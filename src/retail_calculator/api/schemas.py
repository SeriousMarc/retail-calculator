"""
Validation Schemas
"""
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, condecimal


class OrderInput(BaseModel):
    product_amount: condecimal(ge=Decimal('1'), decimal_places=0)
    price_per_product: condecimal(ge=Decimal('0'), decimal_places=2)
    state: str


class Order(OrderInput):
    discount: condecimal(ge=Decimal('0'), decimal_places=2)
    tax: condecimal(gt=Decimal('0'), decimal_places=2)


class OrderOutput(Order):
    gross_price: condecimal(ge=Decimal('0'), decimal_places=2)
    sale: condecimal(ge=Decimal('0'), decimal_places=2)
    net_price: condecimal(ge=Decimal('0'), decimal_places=2)
    stamp: datetime
