class Money(object):
    def __init__(self, amount: int, currency:str) -> None:
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> "Money":
        return Money(self._amount * multiplier, self.currency())

    def __eq__(self, object: "Money") -> bool:
        return self._amount == object._amount and (self._currency == object._currency)

    @staticmethod
    def dollar(amount: int) -> "Money":
        from .dollar import Dollar
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> "Money":
        from .franc import Franc
        return Franc(amount)
    
    def currency(self) -> str:
        return self._currency

    def __repr__(self):
        return str(self._amount) + " " + self._currency