from .expression import Expression
from .money import Money

class Bank(object):
    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(to)