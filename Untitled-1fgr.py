code=input("welcome t the pasword cenerator!\nenter the total number of letters in the password:")
letters=input("enter the number of letters in the password:")
numbers=input("enter the number of numbers in the password:")
symbols=input("enter the number of symbols in the password:")
if int(letters)+int(numbers)+int(symbols)!=int(code):
    print("invald input. the sum of letters, nubmers and symbols doesnt match the password!")
else:
    import random
    import string
    number=random.choices(string.digits, k=int(numbers))
    letter=random.choices(string.ascii_letters, k=int(letters))
    symbol=random.choices(string.punctuation, k=int(symbols))
    final=number+letter+symbol
    random.shuffle(final)
    print("".join(final))
