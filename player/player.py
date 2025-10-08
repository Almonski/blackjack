from hand.hand import Hand
from card.card import Card

class Player():
    def __init__(self, name: str, balance: int = 1000):
        self.name = name
        self.balance = balance
        self.bet = 0
        self.hand = Hand()

    def place_bet(self, amount: int):    
        if amount > self.balance:
            raise ValueError("Too broke")
        self.bet = amount
        self.balance -= amount

    def win_bet(self):
        self.balance += self.bet * 2 
        self.bet = 0

    def blackjack_win(self):
        self.balance += self.bet * 2.5
        self.bet = 0

    def lose_bet(self):
        self.bet = 0

    def show_balance(self):
        return self.balance  

    def hit(self, card):
        self.hand.add_card(card)

    def reset_hand(self):
        self.hand = Hand()
        self.bet = 0

    def return_bet(self):
        self.balance += self.bet
        self.bet = 0
