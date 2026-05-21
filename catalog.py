import os

info = {}


def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")


while True:
    print(
        """menu:
1) add book
2) check out book
3) check in book
4) list book
5) exit"""
    )

    num = input("enter your choice (1_5):")

    if num == "1":
        while True:
            isbn = input("enter ISBN:")

            title = input("enter title:")
            author = input("enter author:")
            info[isbn] = {
                "title": title,
                "author": author,
                "avalible": True,
            }

            print(f"book  {title} by {author} added to the catalog with ISBN {isbn} ")
            choice = input("do you want to add another book? (y/n):").lower()

            if choice != "y":
                break

    if num == "2":
        while True:

            clear()
            isbn = input("enter ISBN to check out:")
            if isbn in info:
                if info[isbn]["avalible"] == True:

                    info[isbn]["avalible"] = False
                else:
                    print("sorry this book is already checked")
            else:
                print("book not found in the catalog")

            choice = input("do you want to check out another book?(y/n):")
            if choice != "y":
                break

    if num == "3":
        while True:
            clear()
            isbn = input("enter ISBN to check in:")
            if isbn in info:
                if info[isbn]["avalible"] == False:
                    info[isbn]["avalible"] = True
                    print(f"book {info[isbn]["title"]} chrcker in sucessfully")
                else:
                    print("the book is already availble in catalog")
            else:
                print("book not found in the catalog")
            choice = input("do you want to check in another book? (y/n):").lower()
            if choice.lower() != "y":
                break

    if num == "4":
        while True:
            clear()
            print("libary catalog:")
            for isbn in info:
                print(
                    f"ISBN: {isbn} , title: {info[isbn]["title"]} , author: {info[isbn]["author"]} , avalible: {info[isbn]["avalible"]} "
                )
            choice = input("do you want to go back to main menu:(y/n):")
            if choice != "y":
                break

    if num == "5":
        print("exiting the program")
        break

    else:
        print("invalid choice")
