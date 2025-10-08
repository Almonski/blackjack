class Card:
    # Alla möjliga färger (suits) i kortleken
    suit = ["Hearts", "Diamonds", "Clubs", "Spades"]

    # Alla möjliga värden/ranks i kortleken
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    # Konstruktor/metod som körs när ett nytt kort skapas
    def __init__(self, suit, rank):
        self.suit = suit  # Färg på kortet (Hearts, Diamonds osv.)
        self.rank = rank  # Rank/värde på kortet (2–10, Jack, Queen, King, Ace)

        # Bestämmer kortets numeriska värde för blackjack
        if rank in ["Jack", "Queen", "King"]:  # Klädda kort
            self.value = 10
        elif rank == "Ace":  # Ess
            self.value = 11
        else:  # Alla siffror 2–10
            self.value = int(rank)

    # Metod som kollar om kortet är ett ess
    def is_ace(self):
        return self.rank == "Ace"

    # Metod som definierar hur kortet ska skrivas ut som text
    def __str__(self):
        return f"{self.rank} of {self.suit}"
