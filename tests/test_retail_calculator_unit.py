"""
UNIT tests
"""
import pytest

from decimal import Decimal

from retail_calculator.api.utils import calculate_discount, calculate_tax

pytestmark = pytest.mark.asyncio


async def test_calculate_discount_with_decimal():
    result = calculate_discount(Decimal('100.0'), Decimal('0.1'))
    assert result == Decimal('99.90')


async def test_calculate_discount_with_negative_values():
    with pytest.raises(ValueError):
        calculate_discount(Decimal('-100.0'), Decimal('0.1'))

    with pytest.raises(ValueError):
        calculate_discount(Decimal('100.0'), Decimal('-0.1'))


async def test_calculate_discount_with_zero_values():
    with pytest.raises(ValueError):
        calculate_discount(Decimal('0'), Decimal('0.1'))

    result = calculate_discount(Decimal('100.0'), Decimal('0'))

    assert result == Decimal('100.0')


async def test_calculate_tax_with_decimal():
    result = calculate_tax(Decimal('100.0'), Decimal('0.1'))

    assert result == Decimal('100.10')


async def test_calculate_tax_with_negative_values():
    with pytest.raises(ValueError):
        calculate_tax(Decimal('-100.0'), Decimal('0.1'))

    with pytest.raises(ValueError):
        calculate_tax(Decimal('100.0'), Decimal('-0.1'))


async def test_calculate_tax_with_zero_values():
    with pytest.raises(ValueError):
        calculate_tax(Decimal('0'), Decimal('0.1'))

    result = calculate_tax(Decimal('100.0'), Decimal('0'))

    assert result == Decimal('100.0')
