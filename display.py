from card.card import Card
from deck.deck import Deck
from hand.hand import Hand
from player.player import Player

def show_title():
    print("\nWELCOME TO BLACKJACK\n")

def show_menu():
    return input("Type 'play' to start or 'exit' to end:\n> ").lower()

def ask_bet():
    return int(input("How much money do you wanna bet?\n> "))

def confirm_bet():
    return input("'Deal' or 'Change' bet?\n> ").lower()

def show_message(msg):
    print(msg)

def show_winner(name):
    print(f"WINNER: {name}\n")

#HIDEN CARD (HAND)

def play_loop():
    show_title()
    player = Player(name="Player", balance=1000)
   
    while player.balance > 0:
        print(f"\nYou have {player.balance} money.")
        choice = show_menu()

        if choice == "exit":
            show_message("Thanks for playing!")
            break
        if choice != "play":
            show_message("Invalid choice, try again.")
            continue

        bet = ask_bet()
        if bet > player.balance:
            show_message("Not enough money!")
            continue

        player.place_bet(bet)

        if confirm_bet() != "deal":
            show_message("Round canceled")
            player.return_bet() 
            continue

        show_message("Round played!")

        player.lose_bet()

    show_message("Game over!")
