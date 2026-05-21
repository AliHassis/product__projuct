age=int(input("enter your age:\n"))
license=input("do you have a license? (yes or no)\n")
if age>=18 and license.lower()=="yes":
    print("you can drive")
elif age<18 or license.lower()=="no":
    print("you dont can drive")
else:
    print("try again")


