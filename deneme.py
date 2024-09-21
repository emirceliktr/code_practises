from copyreg import pickle
from operator import index

import art
import random

#BLACKJACK

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player1 = []
dealer = []

def kart_al(my_list):
    my_list.append(random.choice(cards))

def show_current():
    print(f"Your cards: {player1}, current score: {sum(player1)}")
    print(f"Computer's first card: {dealer[0]}")

def show_final_situation():
    print(f"Your final hand: {player1}, final score: {sum(player1)}")
    print(f"Computer's final hand: {dealer[0]}, final score: {dealer[0]}")

def show_over_situation():
    show_final_situation()
    print("You went over. You Lose ".upper())

def new_card_or_pass():
    kontrol = input("Type 'y' to get another card, type 'n' to pass: ")
    if kontrol == "y":
        kart_al(player1)
        show_current()
        aces_control()
        if sum(player1)>21:
            show_over_situation()
        else:
            new_card_or_pass()
    elif kontrol == "n":
        dealer_get_card()
    else:
        new_card_or_pass()

def dealer_get_card():
    kart_al(dealer)
    aces_control()
    if sum(dealer)<17:
        show_current()
        dealer_get_card()
    elif 17 < sum(dealer) < 21:
        if sum(dealer) < sum(player1):
            show_current()
            show_final_situation()
            print(art.win)
        elif sum(dealer) == sum(player1):
            show_final_situation()
            show_current()
            print(art.draw)
        else:
            show_current()
            show_final_situation()
            print(art.you_lost)
    elif sum(dealer) == 21:
        show_final_situation()
        show_current()
        print(art.you_lost)
    else:
        show_final_situation()
        show_current()
        print(art.win)


def black_jack_the_game():
    answer = input("Do yu want to play a game of Blackjack? Type 'y' or type 'n': ")
    answer.lower()
    if answer == 'n':
        print(art.exit)
    elif answer == "y":
        start_the_game()
    else:
        print("invalid value")
        black_jack_the_game()


def black_jack_control():
    if sum(player1) == 21:
        return True
    else:
        return False
def aces_control():
    if 11 in player1:
        if sum(player1) > 21:
            index_of_11 = player1.index(11)
            player1[index_of_11] = 1
    if 11 in dealer:
        if sum(dealer) > 21:
            index_of_11 = dealer.index(11)
            dealer[index_of_11] = 1


def start_the_game():
    print("\n" * 50)
    print(art.logo)
    kart_al(player1)
    kart_al(dealer)
    kart_al(player1)
    kart_al(dealer)
    show_current()
    if black_jack_control():
        print(art.blackjack)
    else:
        new_card_or_pass()

black_jack_the_game()
