import os
import time


def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")


dollar = {
    "USD": 1.0,
    "EUR": 0.85,
    "EGP": 30.9,
    "RMP": 6.5,
}


def dollars():
    print("welcome to 'currency converter':\n")
    for x in dollar:
        print(f"{x}:{dollar[x]}")


def all():
    clear()
    dollars()

    choice = input("\nchoose a currency to convert from:").upper()
    while True:
        much = float(input("enter the amount:"))
        confirm = input(f"you entered {much} {choice}. confirm? (y/n): ").lower()
      
        if confirm == "y":
            break

    clear()
    dollars()
  
    to_choice = input("choose a currency to convert to:").upper()
  
    print("analyzing your request... please wait.")
    time.sleep(2)
    print(f"checking for {to_choice}'s best rates available..... please wait")
    time.sleep(2)
    print(f"getting a discount ptice for {choice}.... please wait")
    time.sleep(2)
  
    if choice or to_choice not in dollar:
        print("invaild currency. conversion canceled.")
        time.sleep(2)
        all()
    


    monny=round((dollar[to_choice] / dollar[choice]),2)
    final=monny*much

    clear()
    print("\npreparing the deal from {choice} to {to_choice}.... please wait\n")
    time.sleep(1)
    print(f"\nexhange rate : 1 {choice} = {monny} {to_choice}\n")
    time.sleep(1)
    print(f"\n{much} {choice} is equal to {final} {to_choice}")
   
   
    if (input("\ndo you accept this transaction? (y/n):").lower()) != "y":
        print("transaction canceled.\n")
    else:
        print("transaction succeful")
    if(input("\ndo you want to perform another conversion? (y/n): ").lower()) =="y":
        all()
    else:
        print("thanks for using my program")
    

all()
