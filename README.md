# Blackjack

A simple Python implementation of Blackjack with basic betting and automated dealer logic. The user (player) plays against the dealer to get as close as possible to 21 without going over. 

Card values are face value for 2-10. For face cards (King, Queen, Jack), the value is 10 and for Aces, the value is either 1 or 11.

The player starts with 1000 credits and chooses a betting amount. The player is dealt cards and can hit (take a card) or stand (stop taking cards). The dealer hits on 16 or less and stands if 17 or more.

To win, the player’s hand must have a higher total than the dealer's total without busting (being over 21) or if the dealer busts.

## Requirements
- Python 3.x
- colorama (for colors)
- matplotlib (for stats)
- pytest (for running tests)

## Instructions for installation and running

1. Install [Python 3](https://www.python.org/downloads/) if it is not already installed.
2. Install requirements `pip install -r requirements.txt`
3. Download or clone this project folder to your computer.
4. Navigate to the project folder in a terminal (e.g. Hyper, Git Bash, etc.).
5. Start the game by running `python main.py`

## Instructions for running the test files

1. Navigate to the project folder in a terminal (e.g. Hyper, Git Bash, etc.).
2. Run all tests with `pytest`
3. To run a single test, for example `test_card.py`: `pytest test_card.py`

## Who worked on which file

* Elvira - card.py, test_card.py
* Victoria - deck.py, test_deck.py
* Ali - player.py, test_player.py
* Filip - hand.py
* Group - main.py, display.py, colorama and stats integration
