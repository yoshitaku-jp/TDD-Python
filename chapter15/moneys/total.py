from .expression import Expression
from .exchanger import CurrencyExchanger

from .money import Money

class Total(Expression):

    def __init__(self, augend: Expression, addend: Expression) -> None:
        self._augend = augend
        self._addend = addend
    
    def augend(self) -> Money:
        return self._augend

    def addend(self) -> Money:
        return self._addend

    def reduce(self,bank: CurrencyExchanger, currency: str) -> Money:
        amount = self.augend().reduce(bank, currency).amount() + \
            self.addend().reduce(bank, currency).amount()
        return Money(amount, currency)

    def plus(self, addend: Expression):
        pass