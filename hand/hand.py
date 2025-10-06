
class Hand:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        #Lägger till ett kort i handen när funktionen blir kallad
        self.cards.append(card)

    def get_value(self):
        #Beräknar värdet av kortet i handen
        value = 0
        aces = 0

        for card in self.cards:
            value += card.value
            if card.is_ace():
                aces += 1

        #Om man har ett ess värde måste justestas beroende på om värdet av handen > 21 
        while aces > 0 and value > 21:
            value -= 10
            aces -= 1
            return value
        
    def is_blackjack(self):
    #Kollar om handens värde är över 21
        return len(self.cards) == 2 and self.get_value() == 21
        
    def is_over21(self):
        #Kollar om värdet av handen > 21 == du förlorar
        return self.get_value() > 21

    def clear_hand(self):
        #Tömmer handen på kort
        self.cards = []    
