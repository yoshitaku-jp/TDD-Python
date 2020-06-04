class Doolar:

    def __init__(self, amount: int) -> 'null':
        self.amount = amount

    def times(self, multiplier: int) -> "Dollar":
        return Doolar(self.amount * multiplier)