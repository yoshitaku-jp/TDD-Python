from .money import Money

class Franc(Money):

    def __init__(self, amount: int) -> None:
        Money.__init__(self, amount, 'CHF')