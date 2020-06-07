import pytest

from moneys.money import Money
from moneys.dollar import Dollar
from moneys.franc import Franc

class TestMoney():

    def test_multiplication(self):
        five: Money = Money.dollar(5)
        assert Money.dollar(10) == five.times(2)
        assert Money.dollar(15) == five.times(3)

    def test_equality(self):
        assert Dollar(5) == Dollar(5)
        assert Dollar(5) != Dollar(6)
        assert Franc(5) == Franc(5)
        assert Franc(5) != Franc(6)
        assert Dollar(5) != Franc(5)

    def test_franc_multiplication(self):
        five: Money = Money.franc(5)
        assert Money.franc(10) == five.times(2)
        assert Money.franc(15) == five.times(3)