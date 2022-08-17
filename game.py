from Deck import Deck
from Player import Player, Dealer

deck = Deck()
player = Player()
dealer = Dealer()

print("Welcome to Blackjack!")
while True:
    if player.money <= 0:
        print("You've ran out of money. Please restart this program to try again. Goodbye.")
        break
    print(f"You are starting with {player.money}.", end=" ")
    ans = input("Would you like to play a hand?: ")
    if ans.lower() == "no":
        break
    elif ans.lower() == "yes":
        
        bet = input("place your bet: ")
        if not bet.isdigit():
            print("please enter a number")
        elif int(bet) > player.money:
            print("You do not have sufficient funds")
        elif int(bet) < 1:
            print("The minimum bet is $1")
        else:
            deck.deck_shuffle()
            player.first_hand(deck)
            dealer.first_hand(deck)

            print(f"You are dealt {player.hand[0]}, {player.hand[1]}")
            print(f"dealer is dealt {dealer.hand[0]}, Unknown")

            if player.sum_cards() == 21:
                if dealer.sum_cards() < 21:
                    player.money += int(bet) * 1.5
                    print("Blackjack! You win $150 :)")
                if dealer.sum_cards() == 21:
                    print("Both have Blackjack, it's a tie")


            while True:
                hit_stay = input("Would you like to hit or stay? ")
                if hit_stay.lower() == "stay":
                    print(f"dealer is dealt {dealer.hand[0]}, {dealer.hand[1]}")
                    while dealer.sum_cards() < 17:
                        dealer.hit(deck)
                        print(f"dealer is hit {dealer.hand[-1]}")
                        print("dealer now has: ", end=" ")
                        for card in dealer.hand:
                            if dealer.hand.index(card) == len(dealer.hand) - 1:
                                print(card)
                            else:
                                print(card, end=", ")

                    if dealer.sum_cards() > 21:
                        player.money += int(bet)
                        print(f"The dealer busts, you win {bet}")
                    else:
                        if dealer.sum_cards() < player.sum_cards():
                            player.money += int(bet)
                            print(f"You win {bet}")
                        elif dealer.sum_cards() == player.sum_cards():
                            print("You tie. Your bet has been returned.")
                        else:
                            player.money -= int(bet)
                            print(f"The dealer wins, you loose {bet}")

                    deck.restart_deck()
                    player.restart_hand()
                    dealer.restart_hand()
                    break

                if hit_stay == "hit":
                    player.hit(deck)
                    print("Now you have: ", end=" ")
                    for card in player.hand:
                        if player.hand.index(card) == len(player.hand) -1:
                            print(card)
                        else:
                            print(card, end=", ")

                    if player.sum_cards() > 21:
                        print(f"Your hand value is over 21 and you lose {bet}:(")
                        player.money -= int(bet)
                        deck.restart_deck()
                        player.restart_hand()
                        dealer.restart_hand()
                        break
    if ans == "no":
        print("Thanks for playing, Goodbye!")  
        break          
    else:
        print("please answer yes or no.")