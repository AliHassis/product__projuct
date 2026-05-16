import random
import os
import time


def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")


def get_card():
    list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = random.choice(list)
    return cards


def sim(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def win(sum_user, sum_computer):
    result = {
        "draw": "draw\n\n",
        "user_over": "you went over 21, sorry\n\n",
        "computer_over": "computer went over 21,you win\n\n",
        "user_21": "you won with a blackjack\n\n",
        "computer_21": "sorry, computer had a blackjack \n\n",
        "user_win": "you win\n\n",
        "you_lose": "you lose\n\n",
    }

    if sum_user == sum_computer:
        return result["draw"]
    elif sum_user > 21:
        return result["user_over"]
    elif sum_computer > 21:
        return result["computer_over"]
    elif sum_user == 0:
        return result["user_21"]
    elif sum_computer == 0:
        return result["computer_21"]
    elif sum_user > sum_computer:
        return result["user_win"]
    else:
        return result["you_lose"]


def start():

    num_user = [get_card() for _ in range(2)]
    num_computer = [get_card(), get_card()]

    game_continue = True
    while game_continue== True:

        sum_user=sim(num_user)
        sum_computer=sim(num_computer)

        print(f"your cards are {num_user}, current score is {sum_user}")
        print(f"computer's first card is {num_computer[0]}")
        if sum_user==0 or sum_computer==0 or sum_computer>21 or sum_user>21:
            game_continue = False
        else:
            if input("get another card?(y/n)").lower() == "y":
                num_user.append(get_card())
            else:
                game_continue = False
    
    while sum_computer != 0 and sum_computer < 17:
        num_computer.append(get_card())
        sum_computer=sim(num_computer)
      

    print(f"your final hand:v{num_user} with score {sum_user}")
    print(f"computer's final hand is: {num_computer} with score {sum_computer}")
    print(win(sum_user, sum_computer))


while True:
    choice = input(
        """choose a game to start.....

1) froggy
2) twenty one
3) snake
__________
          """
    )

    if choice == "twenty one":
        start()
