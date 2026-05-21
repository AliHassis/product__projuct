import random
import os
import time


def clear():
    os.system("cls.") if os.name == "nt" else os.system("clear")


def card_1():
    list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(list)
    return card


def sum_1(cards):
    if sum(cards) == 21 and len(cards) == 2:
        print("user black")
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(sum_user, sum_computer):
    if sum_user == sum_computer:
        print("draw")
    elif sum_user > 21:
        print("you over 21")
    elif sum_computer > 21:
        print("computer over 21")
    elif sum_user == 0:
        print("you blackjack")
    elif sum_computer == 0:
        print("computer blackjack")
    elif sum_user > sum_computer:
        print("you win")
    else:
        print("you lose")


def game():
    user_card = [card_1() for _ in range(2)]
    computer_card = [card_1() , card_1()]

    while True:
        sum_user=sum_1(user_card)
        sum_computer=sum_1(sum_computer)
        print(f"\n\ncards are {user_card} , currrnt score is {}")






