import pytest
from moneys import doolar

class TestMoney():

    def test_multiplication(self):
        five = doolar.Doolar(5)
        product = five.times(2)
        assert 10 == product.amount
        product = five.times(3)
        assert 15 == product.amount

    def test_equality(self):
        assert doolar.Doolar(5) == doolar.Doolar(5)
        assert doolar.Doolar(5) != doolar.Doolar(6)