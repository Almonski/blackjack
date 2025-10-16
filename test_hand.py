import pytest
from hand.hand import Hand
from card import Card


def test_add_card():
    """Testar att kort läggs till i handen korrekt"""
    hand = Hand("Player")
    card1 = Card("Hearts", "6")
    card2 = Card("Spades", "7")
    
    hand.add_card(card1)
    hand.add_card(card2)
    
    assert len(hand.cards) == 2
    assert hand.cards[0] == card1
    assert hand.cards[1] == card2


def test_get_value():
    """Testar att handens värde beräknas korrekt"""
    hand = Hand("Player")
    card1 = Card("Hearts", "6")
    card2 = Card("Spades", "7")
    
    hand.add_card(card1)
    hand.add_card(card2)
    
    assert hand.get_value() == 13