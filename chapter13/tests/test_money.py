import pytest

from moneys.money import Money
from moneys.bank import Bank
from moneys.total import Total

class TestMoney():

    def test_multiplication(self):
        five: Money = Money.dollar(5)
        assert Money.dollar(10) == five.times(2)
        assert Money.dollar(15) == five.times(3)

    def test_equality(self):
        assert Money.dollar(5) == Money.dollar(5)
        assert Money.dollar(5) != Money.dollar(6)
        assert Money.dollar(5) != Money.franc(5)

    def test_currency(self):
        assert "USD" == Money.dollar(1).currency()
        assert "CHF" == Money.franc(1).currency()

    def test_simple_addition(self):
        five = Money.dollar(5)
        total = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(total, 'USD')
        assert Money.dollar(10) == reduced

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        result = five.plus(five)
        total: Total = result
        assert five == total.augend()
        assert five == total.addend()

    def test_reduce_sum(self):
        total = Total(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(total, "USD")
        assert Money.dollar(7) == result

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        assert Money.dollar(1) == result