from .money import Money

class Franc(Money):

    def __init__(self, amount: int) -> None:
        Money.__init__(self, amount, 'CHE')

    def times(self, multiplier: int) -> "Money":
        return Franc(self._amount * multiplier)