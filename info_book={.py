info = {}

while True:
    print("contact management")
    print()
    print("1- add a contact")
    print("2- view a contact")
    print("3- edit a conact")
    print("4- exit")

    number = input("please choose a number from 1-4:")

    if number == "1":
        id_user = input("please enter the contact id:")
        name_user = input("please type a name:")
        phone_user = input("please type a phone number:")
        while not phone_user.isdigit():
            print("choose a number\n")
            phone_user = input("please type a phone number:")

        info[id_user] = {"title": name_user, "number": phone_user}

    elif number == "2":
        print(info)

    elif number == "3":
        new_id = input("please enter an id edit")
        if new_id in info:
            new_name = input("enter a new name:")
            new_phone = input("enter a new number:")
            while not new_phone.isdigit:
                print("choose a number\n")
                new_number = input("please type a phone number")
            info[new_id]["title"] = new_name
            info[new_id][number] = new_phone
            print("success.......\n")
        else:
            print(f"the {new_id} is not found")

    elif number == "4":
        break

    else:
        print("invalid selection")
