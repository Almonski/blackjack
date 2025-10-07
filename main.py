from card.card import Card
from deck.deck import Deck
from hand.hand import Hand
from player.player import Player
import display

### This file controls the game logic ###

    # ---GAME INITIALIZATION---
    # SHOW TITLE SCREEN
    # CREATE GAME OBJECTS
        # CREATE DECK (SHUFFLED)
        # CREATE THE PLAYER (WITH STARTING BALANCE)
        # CREATE THE DEALER (JUST AN INSTANCE OF HAND OBJECT, UNLESS WE MAKE DEALER CLASS)


    # ---MAIN GAME LOOP---
        # WHILE PLAYER HAS MONEY
            # SHOW BALANCE 
            # ASK IF PLAYER WANTS TO PLAY OR EXIT 
            # IF EXIT -> SHOW GOODBYE MESSAGE, BREAK LOOP 
            # IF INVALID INPUT, ASK AGAIN


    # ---BETTING PHASE---
        # ASK HOW MUCH MONEY TO BET
        # CHECK IF BET IS VALID (NOT MORE THAN BALANCE) 
        # SUBTRACT BET FROM BALANCE 
        # CONFIRM BET (DEAL OR CHANGE) 
            # IF CHANGE: RETURN BET, CANCEL ROUND


    # ---DEALING PHASE---
        # CLEAR BOTH HANDS (NO OLD CARDS REMAIN)
        # DEAL 2 CARDS TO PLAYER
        # DEAL 2 CARDS TO DEALER
        # SHOW FULL PLAYER HAND + VALUE
        # SHOW DEALER'S FIRST CARD + ONE HIDDEN CARD


    # ---CHECK FOR BLACKJACK---
        # IF PLAYER HAS BLACKJACK -> INSTANT WIN
        # IF NOT -> CONTINUE TO PLAYER'S TURN


    # ---PLAYER'S TURN---
        # LOOP UNTIL PLAYER STANDS OR BUSTS
            # ASK IF HIT OR STAND
            # IF HIT: DRAW A CARD, UPDATE HAND, SHOW NEW VALUE
            # IF VALUE > 21, PLAYER BUSTS, LOSE BET


    # ---DEALER'S TURN---
        # REVEAL HIDDEN CARD
        # WHILE DEALER'S VALUE < 17: HIT!
        # SHOW EACH DEALER DRAW
        # STOP WHEN DEALER'S HAND >= 17 OR BUSTS


    # ---COMPARE HANDS---
        # IF DEALER BUSTS: PLAYER WINS
        # IF PLAYER'S VALUE > DEALER'S VALUE: PLAYER WINS
        # IF DEALER'S VALUE > PLAYER'S VALUE: DEALER WINS
        # IF EQUAL -> PUSH (RETURN BET TO PLAYER)


    # ---UPDATE BALANCE---
        # IF PLAYER WINS: USE win_bet() FROM player.py TO ADD WINNINGS
        # IF PLAYER LOSES: USE lose_bet() FROM player.py TO SHOW BET IS GONE
        # IF TIE: RETURN BET TO BALANCE


    # ---LOOP END---
        # IF BALANCE > 0, CONTINUE BACK TO MAIN GAME LOOP'
        # IF BALANCE = 0, SHOW GAME OVER MESSAGE


if __name__ == "__main__":
    #main game loop should be here so it runs when the program is opened