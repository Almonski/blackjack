from hand.hand import Hand

class Player(Hand):
    def __init__(self, name: str, balance: int = 0,):
        self.name = name
        self.balance = balance
        self.bet = 0

    def place_bet(self, amount: int):    
        if amount > self.balance:
            raise ValueError("Too broke")
        self.bet = amount
        self.balance -= amount

    def win_bet(self):
        self.balance += self.bet * 2
        self.bet = 0

    def lose_bet(self):
        self.bet = 0

    def show_balance(self):
        return self.balance        

    def return_bet(self):
        pass
