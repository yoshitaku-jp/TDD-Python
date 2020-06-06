class Money:
    def __init__(self, amount: int) -> 'null':
        self._amount = amount

    def __eq__(self, object: "Money") -> bool:
        return self._amount == object._amount