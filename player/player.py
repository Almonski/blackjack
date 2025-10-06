class Player:
    def __init__(self, name: str, balance: int = 0):
        self.name = name
        self.balance = balance
        self.bet = 0

    def place_bet(self, amount: int):    
        if amount > self.balance:
            raise ValueError("Too broke")
        self.bet = amount
        self.balance -= amount