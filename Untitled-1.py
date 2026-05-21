rules=input("welcome to the rock, paper , scissors game:\npress enter to cotinue or type (help) for the rules help:"
"").lower()
if rules == "help":
    print("""                 *****RULES*****
                 1)gdhfiehfeif
                 2)fhvihgigh
                 3)kfnbvkfdn
                 4)nkefehkd""")
    expect=input("enter yout choice (rock, paper, scissors):").lower()
else:
    expect=input("enter yout choice (rock, paper, scissors):").lower()


import random
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
comexpect=random.randint(0,2)
if comexpect ==0:
    com1expect=rock
elif comexpect==1:
    com1expect=paper
else:
    com1expect=scissors


if expect =="rock":
   print("you choicer:")
   print(rock)
   print("computer choice:")
   print(com1expect)
   if com1expect==rock:
       print("taadl")
   elif com1expect==paper:
       print("you lose")
   else :
       print("you win")

elif expect =="paper":
    print("you choicer:")
    print(paper)
    print("computer choice:")
    print(com1expect)
    if com1expect==rock:
       print("you win")
    elif com1expect==paper:
       print("taadl")
    else :
       print("you lose")

elif expect=="scissors":
    print("you choicer:")
    print(scissors)
    print("computer choice:")
    print(com1expect)
    if com1expect==rock:
       print("you lose")
    elif com1expect==paper:
       print("you win")
    else :
       print("taadl")
else:
    print("invalid choice ")