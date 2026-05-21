import string

letter = string.ascii_lowercase


user_message = input("enter a message:")
user_number = int(input("enter a shift number:"))


def info(message, number):
    secret = ""
    for x in message:
        if x.lower() in letter:
            num = (letter.index(x.lower())-number) %26
            oop=letter[num]
            if x.isupper():
                 oop=letter[num].upper()
            secret+=oop
        else:
                secret += x
    print(secret)
    print(message)


info(user_message, user_number)
