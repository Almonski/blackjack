import random
from Card import Card
# !!! UPDATE for Card later !!!

# Klassen Deck representerar en klassisk kortlek med 52 kort, ska hantera
# skapandet av kortleken, blandning av kortleken och utdelning av kort

class Deck:
    def __init__(self):
        self.deck = []
        self.create_deck()
        self.shuffle()
    
    def create_deck(self):
        # skapar alla 52 kort genom att loopa genom valörer
        # och färger och sen lägger in dem i en variabel "deck"
        pass
    # !!! ADD LATER !!!

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        # tar bort "oversta kortet i en kortlek med hjälp av "pop"
        if self.deck:
            return self.deck.pop(0)
        else:
            return None

    def remaining_cards(self):
        # returnerar hur många kort som är krav i kortleken
        return len(self.deck)
    
    def reset_deck(self):
        # skapar en ny kortlek, tömmer, återskapar och blandar
        self.create_deck()
        self.shuffle()

if __name__ == "__main__":
    #testning
    pass
    # !!! UPDATE LATER TO ADD TEST CODE !!!

    # Deck testing
    # deck = Deck()
    # deck.create_deck()
    # deck.shuffle()
    # print(deck.draw_card())
    # deck.remaining_cards()
    # deck.reset_deck()
    # print(self.deck)