from .money import Money

class Dollar(Money):

    def __init__(self, amount: int) -> None:
        Money.__init__(self, amount, 'USD')