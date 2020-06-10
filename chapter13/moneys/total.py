from .expression import Expression
from .money import Money

class Total(Expression):

    def __init__(self, augend: Money, addend: Money) -> None:
        self._augend = augend
        self._addend = addend
    
    def augend(self) -> Money:
        return self._augend

    def addend(self) -> Money:
        return self._addend

    def reduce(self, currency: str) -> Money:
        amount = self.augend().amount() + self.addend().amount()
        return Money(amount, currency)