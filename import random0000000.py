import random

coin=int(input("""welcome to the coin guessing game!
choose a method to toss the coin:
1.using random.random()
2.using random.randint()
enter your choise (1 or 2):"""))

if coin==1:
    if random.random()>=0.5:
        expect="heads" 
    else:
        expect="tails"
elif coin==2 :
    if random.randint(0,1)==0:
        expect="heads"
    else:
        expect="tails"
else :
    print("invaild choice please celect either 1 or 2")  




expect1=input("enter your guess ( heads or tails):")
if expect1.lower()==expect:
    print("congratulations! you won")
else:
    print("sorry you lost")

print(f"the expecttions coin toss result was :{expect}")
