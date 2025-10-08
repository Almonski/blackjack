import pytest
from player.player import Player

def test_place_bet():
    player = Player("Test", balance=1000)
    player.place_bet(200)
    assert player.bet == 200
    assert player.balance == 800

def test_blackjack_win():
    player = Player("Test", balance=1000)
    player.place_bet(200)
    player.blackjack_win()
    assert player.balance == 1000 + 200*2.5  # 1500