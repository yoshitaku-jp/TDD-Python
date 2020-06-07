from .money import Money

class Dollar(Money):

    def __init__(self, amount: int) -> None:
        Money.__init__(self, amount, 'USD')

    def times(self, multiplier: int) -> "Money":
        return Dollar(self._amount * multiplier)
