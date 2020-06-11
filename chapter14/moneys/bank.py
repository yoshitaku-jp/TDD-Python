from .expression import Expression
from .exchanger import CurrencyExchanger

from .money import Money

class Bank(CurrencyExchanger):
    def __init__(self):
        self._rates = dict()

    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)

    def add_rate(self, fromcurr: str, tocurr: str, rate: int) -> None:
        self._rates[(fromcurr, tocurr)] = rate

    def rate(self, fromcurr: str, tocurr: str) -> int:
        if fromcurr == tocurr:
            return 1
        return self._rates.get((fromcurr, tocurr))