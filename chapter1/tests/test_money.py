import pytest
from moneys import doolar

class TestMoney():

    def test_multiplication(self):
        five = doolar.Doolar(5)
        five.times(2)
        assert 10 == five.amount