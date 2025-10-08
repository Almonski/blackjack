import pytest
from card.card import Card

def test_number_and_face_cards():
    # Testar numeriska kort (7) och klädda kort (King)
    card1 = Card("Hearts", "7")
    card2 = Card("Spades", "King")
    
    # Kolla att värdet på numeriskt kort är korrekt och att det inte är ess
    assert card1.value == 7
    assert not card1.is_ace()
    
    # Kolla att klätt kort har värde 10 och inte är ess
    assert card2.value == 10
    assert not card2.is_ace()

def test_ace_and_str():
    # Testar ess-kort och strängrepresentation
    card = Card("Diamonds", "Ace")
    
    # Ess ska ha värde 11 och identifieras korrekt
    assert card.value == 11
    assert card.is_ace()
    
    # Kolla att strängrepresentationen är korrekt
    assert str(card) == "Ace of Diamonds"
