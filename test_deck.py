import pytest
from deck.deck import Deck

# Test that deck starts with 52 cards
def test_deck_starts_with_52():
    deck = Deck()
    assert deck.remaining_cards() == 52

# Test that drawing reduces the deck size by 1
def test_drawing_reduceby1():
    deck = Deck()
    pre_draw = deck.remaining_cards()
    deck.draw_card()
    post_draw = deck.remaining_cards()
    assert pre_draw - post_draw == 1

# Test that shuffle() shuffles the cards
def test_shuffle():
    deck = Deck()
    pre_shuffle = deck.deck.copy()
    deck.shuffle()
    post_shuffle = deck.deck
    assert pre_shuffle != post_shuffle

# Test that reset_deck() restores to 52 cards
def test_reset_to52():
    deck = Deck()
    deck.reset_deck()
    remaining = deck.remaining_cards()
    assert remaining == 52


if __name__ == "__main__":
    test_deck_starts_with_52()
    test_drawing_reduceby1()
    test_shuffle()
    test_reset_to52()