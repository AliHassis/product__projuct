import random
import os
import time

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def get_card():
    # قمنا بتغيير اسم المتغير لـ cards_pool لتجنب الكلمة المحجوزة list
    cards_pool = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards_pool)

def sim(cards):
    # إذا كان المجموع 21 من كرتين فقط، فهذا Blackjack (نعبر عنه بـ 0)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # تحويل قيمة الآس (11) إلى (1) إذا تجاوز المجموع 21
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def win(sum_user, sum_computer):
    result = {
        "draw": "It's a Draw! 🤝\n\n",
        "user_over": "You went over 21. You lose! 💥\n\n",
        "computer_over": "Computer went over 21. You Win! 🎉\n\n",
        "user_21": "Blackjack! You win! 🏆\n\n",
        "computer_21": "Computer has a Blackjack. You lose! 😢\n\n",
        "user_win": "Congratulations! You win! 🥇\n\n",
        "you_lose": "Sorry, you lose! 🤖\n\n",
    }

    # منطق تحديد الفائز بدقة
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
    clear()
    print("--- Welcome to Twenty One (Blackjack) ---")
    num_user = [get_card() for _ in range(2)]
    num_computer = [get_card(), get_card()]

    game_continue = True
    while game_continue:
        sum_user = sim(num_user)
        sum_computer = sim(num_computer)

        print(f"\nYour cards: {num_user}, current score: {sum_user}")
        print(f"Computer's first card: {num_computer[0]}")
        
        # التوقف إذا وصل أحد اللاعبين لـ Blackjack أو تخطى 21
        if sum_user == 0 or sum_computer == 0 or sum_user > 21:
            game_continue = False
        else:
            action = input("Get another card? (y/n): ").lower()
            if action == "y":
                num_user.append(get_card())
            else:
                game_continue = False
    
    # ذكاء اصطناعي للكمبيوتر: يستمر في السحب طالما مجموعه أقل من 17
    while sum_computer != 0 and sum_computer < 17:
        num_computer.append(get_card())
        sum_computer = sim(num_computer)
      
    print("\n==============================")
    print(f"Your final hand: {num_user} with score: {sum_user}")
    print(f"Computer's final hand: {num_computer} with score: {sum_computer}")
    print("==============================")
    print(win(sum_user, sum_computer))

# القائمة الرئيسية لتشغيل الألعاب
while True:
    choice = input(
        """Choose a game to start:
1) froggy
2) twenty one
3) snake
4) exit
________
👉 """
    ).lower()

    if choice == "twenty one" or choice == "2":
        start()
    elif choice == "exit" or choice == "4":
        print("Goodbye!")
        break
    else:
        print("Game not found or under development. Try selecting 'twenty one'.\n")
