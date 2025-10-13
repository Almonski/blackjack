import pytest
from deck.deck import Deck

# Test that deck starts with 52 cards
def test_deck_starts_with_52():
    deck = Deck()                           # create a deck of cards
    assert deck.remaining_cards() == 52     # return how many cards are in the deck list

# Test that drawing reduces the deck size by 1
def test_drawing_reduceby1():
    deck = Deck()                       # create a deck of cards
    pre_draw = deck.remaining_cards()   # count the deck 
    deck.draw_card()                    # draw the last card (top card) in the deck
    post_draw = deck.remaining_cards()  # count the deck after one card was drawn
    assert pre_draw - post_draw == 1    # test that the difference before/after draw is 1 (only one card taken)

# Test that shuffle() shuffles the cards
def test_shuffle():
    deck = Deck()                       # create a deck of cards
    pre_shuffle = deck.deck.copy()
    deck.shuffle()
    post_shuffle = deck.deck
    assert pre_shuffle != post_shuffle

# Test that reset_deck() restores to 52 cards
def test_reset_to52():
    deck = Deck()                       # create a deck of cards
    deck.reset_deck()                   # tömmer kortleklistan, återskapar kortleken och blandar den
    assert deck.remaining_cards() == 52 # kolla att den nya kortleken har 52 kort


if __name__ == "__main__":
    test_deck_starts_with_52()
    test_drawing_reduceby1()
    test_shuffle()
    test_reset_to52()