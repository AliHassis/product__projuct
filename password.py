print("welcome to the pasword cenerator!") 
code=int(input("enter the total number of letters in the password:"))
letters=int(input("enter the number of letters in the password:"))
numbers=int(input("enter the number of numbers in the password:"))
symbols=int(input("enter the number of symbols in the password:"))
if letters+ numbers+ symbols!=code:
    print("invald input. the sum of letters, nubmers and symbols doesnt match the password!")
else:
    import random
    import string
    number=random.choices(string.digits, k=numbers)
    letter=random.choices(string.ascii_letters, k=letters)
    symbol=random.choices(string.punctuation, k=symbols)
    final=number+letter+symbol
    random.shuffle(final)
    print("generated password:")
    print("".join(final))
