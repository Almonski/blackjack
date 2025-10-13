import random
from card.card import Card
# Klassen Deck representerar en klassisk kortlek med 52 kort, ska hantera
# skapandet av kortleken, blandning av kortleken och utdelning av kort

class Deck:
    def __init__(self):
        self.deck = []
        self.create_deck()
        self.shuffle()
    
    def create_deck(self):
        # skapar alla 52 kort genom att loopa genom färger och
        # valörer och sen lägger in dem i den tom listvariabel "deck"        
        for suit in Card.suit:
            for rank in Card.ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):
        # blandar kortlek ("deck") listan
        random.shuffle(self.deck)

    def draw_card(self):
        # tar bort översta kortet i en kortlek med hjälp av "pop"
        if self.deck:
            return self.deck.pop(-1)
        else:
            return None

    def remaining_cards(self):
        # returnerar hur många kort som är krav i kortleken
        return len(self.deck)
    
    def reset_deck(self):
        # tömmer kortleklistan, återskapar kortleken och blandar den
        self.deck = []
        self.create_deck()
        self.shuffle()
