class Card:
    suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = [ "2", "3","4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank 

        if rank in["Jack","Queen","King"]:
            self.value = 10
        elif rank == "Ace":
            self.value = 11
        else:
            self.value = int(rank)

    def is_ace (self):
        return self.rank == "Ace"

    def __str__ (self):
        return f"{self.rank} of {self.suit}"