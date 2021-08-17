"""
Calculation Utilities
"""
from decimal import Decimal


def calculate_discount(price: Decimal, rate: Decimal) -> Decimal:
    if rate < Decimal('0'):
        raise ValueError('Discount rate lower than 0')

    if price <= Decimal('0'):
        raise ValueError('Discount price lower or equal to 0')

    return price - (price * rate / 100)


def calculate_tax(price: Decimal, rate: Decimal) -> Decimal:
    if rate < Decimal('0'):
        raise ValueError('Tax rate lower than 0')

    if price <= Decimal('0'):
        raise ValueError('Tax price lower or equal to 0')

    return price + (price * rate / 100)
