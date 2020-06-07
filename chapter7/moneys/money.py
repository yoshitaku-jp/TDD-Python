class Money:
    def __init__(self, amount: int) -> 'null':
        self._amount = amount

    def __eq__(self, object: "Money") -> bool:
        return self._amount == object._amount and (self.__class__.__name__ == object.__class__.__name__)