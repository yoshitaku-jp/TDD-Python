from abc import ABCMeta, abstractclassmethod

class Money(metaclass=ABCMeta):
    def __init__(self, amount: int) -> None:
        self._amount = amount

    @abstractclassmethod
    def times(self, multiplier: int) -> "Money":
        pass

    def __eq__(self, object: "Money") -> bool:
        return self._amount == object._amount and (self.__class__.__name__ == object.__class__.__name__)

    @staticmethod
    def dollar(amount: int) -> "Money":
        from .dollar import Dollar
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> "Money":
        from .franc import Franc
        return Franc(amount)