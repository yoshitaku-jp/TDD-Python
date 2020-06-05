class Dollar:

    def __init__(self, amount: int) -> 'null':
        self._amount = amount

    def __eq__(self, object: "Dollar") -> bool:
        return self._amount == object._amount

    def times(self, multiplier: int) -> "Dollar":
        return Dollar(self._amount * multiplier)

