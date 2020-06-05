class Doolar:

    def __init__(self, amount: int) -> 'null':
        self.amount = amount

    def __eq__(self, object: "Dollar") -> bool:
        return self.amount == object.amount

    def times(self, multiplier: int) -> "Dollar":
        return Doolar(self.amount * multiplier)

