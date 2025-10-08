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
        # skapar alla 52 kort genom att loopa genom valörer
        # och färger och sen lägger in dem i en variabel "deck"        
        for suit in Card.suit:
            for rank in Card.ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):
        # blandar kortlek
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
        # skapar en ny kortlek, tömmer, återskapar och blandar
        self.deck = []
        self.create_deck()
        self.shuffle()

if __name__ == "__main__":
    import random
    from card.card import Card
    print("Testing: create deck")
    deck = Deck()
    print(f"Created a deck with {deck.remaining_cards()} cards.")

    print("Testing: drawing cards")
    for _ in range(5):
        draw_card()
    print(f"Drew card: {card.rank} of {card.suit}")    

    print("TESTING: CHECK HOW MANY CARDS REMAINING")
    print(f"There are {deck.remaining_cards()} cards remaining.")

    print("TESTING: AFTER RESET, HOW MANY CARDS IN DECK?")
    deck.reset_deck()
    print(f"There are {deck.remaining_cards()} cards remaining.")
