#Import time för pauser mellan utskrifter
import time
# Importerar klasserna Card, Deck, Hand och Player från deras respektive mappar
from card.card import Card
from deck.deck import Deck
from hand.hand import Hand
from player.player import Player

# Funktion som visar en välkomsttext
def show_title():
    print("\nWELCOME TO BLACKJACK\n")

# Funktion som visar menyn där spelaren får välja att spela eller avsluta
def show_menu():
    return input("Type 'play' to start or 'exit' to end:\n> ").lower()

# Funktion som frågar spelaren hur mycket pengar de vill satsa
def ask_bet(player: Player):
    while True:
        try:
            amount = int(input("How much money do you wanna bet?\n> "))
            player.place_bet(amount)
            return amount
        except ValueError as e:
            # check type of ValueError
            if str(e) == "Too broke":
                print("🛑 You don't have enough money. Try a smaller bet.")
            else:
                print("🛑 Invalid input. Please enter a number.")

# Funktion som låter spelaren bekräfta eller ändra sin insats
def confirm_bet():
    return input("'Deal' or 'Change' bet?\n> ").lower()

# Funktion som visar ett meddelande på skärmen
def show_message(msg, delay=1.0):
    print(msg)
    time.sleep(delay)

# Funktion som visar vinnaren av rundan
def show_winner(name):
    print(f"WINNER: {name}\n")
    time.sleep(1.5)

# ----------------------------------------------------
# HUVUDLOOP FÖR SPELET
# ----------------------------------------------------
def play_loop():
    show_title()  # Visar spelets titel
    player = Player(name="Player", balance=1000)  # Skapar en spelare med ett startkapital på 1000
    dealer = Hand("Dealer") # Skapar en dealer

    # Spelet fortsätter så länge spelaren har pengar kvar
    while player.balance > 0:
        print(f"\nYou have {player.balance} money.")  # Visar hur mycket pengar spelaren har kvar
        choice = show_menu()  # Frågar om spelaren vill spela eller avsluta

        # Om spelaren väljer att avsluta spelet
        if choice == "exit":
            show_message("Thanks for playing!", delay=0.5)
            break  # Avslutar while-loopen

        # Om spelaren inte skriver "play" eller "exit"
        if choice != "play":
            show_message("Invalid choice, try again.", delay=0.5)  # Felmeddelande
            continue  # Går tillbaka till början av loopen

        # Frågar hur mycket spelaren vill satsa
        bet = ask_bet(player)

        # Frågar om spelaren vill "deal" (spela rundan) eller "change" (ändra insats)
        if confirm_bet() != "deal":
            show_message("Round canceled", delay=0.5)  # Meddelar att rundan avbryts
            player.return_bet()  # Ger tillbaka insatsen till spelaren
            continue  # Startar om loopen utan att spela rundan
        # Skapa en ny kortlek varje runda
        show_message("\nDealer shuffles the deck", delay=1.0)
        deck = Deck()

        # Töm tidigare händer
        player.clear_hand()
        dealer.clear_hand()
        
        # Dela ut startkorten
        show_message("Dealing cards...", delay=1.0)

        player.hit(deck.draw_card())
        dealer.add_card(deck.draw_card())
        player.hit(deck.draw_card())
        dealer.add_card(deck.draw_card())

        # Visa startkorten
        player.show_hand(hide_card=False, delay=True)
        dealer.show_hand(hide_card=True, delay=True)
        
        if player.is_blackjack():
            #Om spelaren har blackjack, visar dealern också sina kort
            show_message("\nDealer reveals their hand:")
            dealer.show_hand(hide_card=False, delay=True)

            if dealer.is_blackjack():
                show_message("\nBoth player and dealer have Blackjack! It's a push!")
                player.return_bet()
                continue  # rundan avslutas
            else:
                show_message("\nBLACKJACK! You win! 🎉")
                player.blackjack_win()
                show_winner(player.name)
                continue  # rundan avslutas


        if dealer.is_blackjack():
            show_message("\nDealer reveals their hand:")
            dealer.show_hand(hide_card=False, delay=True)
            show_message("\nDealer has Blackjack! You lose 😔")
            player.lose_bet()
            show_winner(dealer.name)
            continue
        while True:
            choice = input("\nDo you want to 'hit' or 'stand'?\n> ").lower()

            if choice == "hit":
                # Spelaren får ett kort till
                player.hit(deck.draw_card())
                player.show_hand()

                # Kolla om spelaren gått över 21
                if player.is_over21():
                    show_message("\nBUST! You went over 21 😭")
                    player.lose_bet()
                    show_winner("Dealer")
                    break  # rundan slut
                
                if player.get_value() == 21:
                    show_message("\n21! You automatically stand.")
                    break

            elif choice == "stand":
                show_message("\nYou chose to stand.")
                break  # avsluta spelarens tur

            else:
                show_message("Invalid choice, type 'hit' or 'stand'.") 
        
        if player.is_over21():
            continue
        
        #Dealerns tur
        show_message("\nDealer reveals their hand")
        dealer.show_hand(hide_card=False, delay=True)

        while dealer.get_value() < 17:
            show_message("\nDealer decides to hit")
            dealer.add_card(deck.draw_card())
            dealer.show_hand(hide_card=False, delay=True)

        if dealer.is_over21():
            show_message("\nDealer BUST! You win! 🎉")
            player.win_bet()
            show_winner(player.name)
            continue

        if dealer.get_value() >= 17:
            show_message("\nDealer decides to stand")

        dealer_value = dealer.get_value()
        player_value = player.get_value()
        print(f"\nFinal scores: \nYou: {player_value}  \nDealer: {dealer_value}")

        if player_value > dealer_value:
            show_message("\nYou win!", delay=2)
            player.win_bet()
            show_winner(player.name)
        elif player_value < dealer_value:
            show_message("\nDealer wins!", delay=1.5)
            player.lose_bet()
            show_winner(dealer.name)
        else:
            show_message("\nIt's a push!", delay=1.5)
            player.return_bet()
            

            
    # När spelaren har 0 pengar kvar avslutas spelet
    show_message("Game over! You're broke.")
