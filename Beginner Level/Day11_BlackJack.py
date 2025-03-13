# Author : Manav
# Task : BlackJack Game

import random

# Defining the cards and their values
card_val_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

# Defining the card selecting function for user
def sel_card_user():
    card = random.choice(card_val_lst)
    return card

# Defining the card selecting function for computer
def sel_card_cmp():
    card = random.choice(card_val_lst)
    return card

print("Welcome to BlackJack!")
print()

# Setting up procedure and win conditions for game
while True:
    print()
    chi = input("Do you want to play BlackJack! (Y/N): ")

    if chi.lower() == "y":
        print()

        is_game_over = False
        while not(is_game_over):
            
            user_cards = []
            cmp_cards = []

            print("Assigning cards to Player and Computer!")
            print()

            user_cards.append(sel_card_user())
            user_cards.append(sel_card_user())
            user_ttl_scr = user_cards[0] + user_cards[1]

            print(f"Player's cards are {user_cards} and they sum up to {user_ttl_scr}!")

            cmp_cards.append(sel_card_cmp())
            cmp_ttl_scr = cmp_cards[0]
            
            print(f"Computer's First Card is {cmp_cards[0]}!")

            print()
            ch = input("Do you want to draw a card or pass (draw/pass): ")
            print()

            if ch == "draw":


                user_cards.append(sel_card_user())
                user_ttl_scr += user_cards[2]
                print(f"Player's final hand are {user_cards} and they sum up to {user_ttl_scr}!")



                ch_cmp = random.randint(0,1)



                if ch_cmp == 0:
                    cmp_cards.append(sel_card_cmp())
                    cmp_ttl_scr += cmp_cards[1]
                    print(f"Computer's new cards are {cmp_cards} and they sum up to {cmp_ttl_scr}!")
                else:
                    print(f"Computer's final hand has {cmp_cards} and they sum up to {cmp_ttl_scr}!")



                print()
                if user_ttl_scr > 21 and cmp_ttl_scr <= 21:
                    print("Over 21! You Lose!")
                    is_game_over = True

                elif user_ttl_scr <= 21 and cmp_ttl_scr > 21:
                    print("Computer went Over 21! You Win!")
                    is_game_over = True

                elif user_ttl_scr == 21 and cmp_ttl_scr == 21:
                    print("Both socred 21! That's a Draw!")
                    is_game_over = True

                elif ((user_ttl_scr < 21) and (cmp_ttl_scr < 21)) and (cmp_ttl_scr > user_ttl_scr):
                    print("You Lose!")
                    is_game_over = True

                elif ((user_ttl_scr < 21) and (cmp_ttl_scr < 21)) and (cmp_ttl_scr < user_ttl_scr):
                    print("You Win!")
                    is_game_over = True

                else: 
                    continue
            


            else: 
                ch_cmp = random.randint(0,1)
                if ch_cmp == 0:
                    cmp_cards.append(sel_card_cmp())
                    cmp_ttl_scr += cmp_cards[1]
                    print(f"Computer's new cards are {cmp_cards} and they sum up to {cmp_ttl_scr}!")
                else:
                    print(f"Computer's final hand has {cmp_cards} and they sum up to {cmp_ttl_scr}!")


                print()
                if user_ttl_scr > 21 and cmp_ttl_scr <= 21:
                    print("Over 21! You Lose!")
                    is_game_over = True

                elif user_ttl_scr <= 21 and cmp_ttl_scr > 21:
                    print("Computer went Over 21! You Win!")
                    is_game_over = True

                elif user_ttl_scr == 21 and cmp_ttl_scr == 21:
                    print("Both scored 21! That's a Draw!")
                    is_game_over = True

                elif ((user_ttl_scr < 21) and (cmp_ttl_scr < 21)) and (cmp_ttl_scr > user_ttl_scr):
                    print("You Lose!")
                    is_game_over = True

                elif ((user_ttl_scr < 21) and (cmp_ttl_scr < 21)) and (cmp_ttl_scr < user_ttl_scr):
                    print("You Win!")
                    is_game_over = True

                else: 
                    continue

    else:
        print("Thanks for Playing!")
        break       
