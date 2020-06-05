class Franc:

    def __init__(self, amount: int) -> 'null':
        self._amount = amount

    def __eq__(self, object: "Franc") -> bool:
        return self._amount == object._amount

    def times(self, multiplier: int) -> "Franc":
        return Franc(self._amount * multiplier)

