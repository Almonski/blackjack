from hand.hand import Hand
from card.card import Card

class Player(Hand):
    def __init__(self, name: str, balance: int = 1000):
        super().__init__(name)
        self.name = name
        self.balance = balance
        self.bet = 0
        

    def place_bet(self, amount: int):    
        if amount > self.balance:
            raise ValueError("Too broke")
        self.bet = amount
        if amount <= 0:
            raise ValueError("Can't place a negative bet")

    def win_bet(self):
        self.balance += self.bet
        self.bet = 0

    def blackjack_win(self):
        self.balance += self.bet * 1.5
        self.bet = 0

    def lose_bet(self):
        self.bet -= self.balance
        self.bet = 0

    def show_balance(self):
        return self.balance  

    def hit(self, card):
        self.add_card(card)

    def reset_hand(self):
        for card in self.cards:
            print(f"Removing {card} from hand...")

        self.clear_hand()
        self.bet = 0

    def return_bet(self):
        self.bet = 0
