import os
import time

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")


class user:
    def __init__(self, first_name, last_name, email, password, status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status

    def display(self):
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")
        print(f"email: {self.email}")
        print(f"status: {self.status}")
        print("___________________")



def create_user():
    first_name=input("enter first name: ")
    last_name=input("enter last name: ")
    email=input("enter your email: ")
    password=input("enter your password: ")

    return user(first_name, last_name, email, password)

        
users={}

def game():
    while True:
        choice=input("""welcome to user managment\n
choose an action:
1. add new user
2. display all user
3. exit\n
enter your choice: """)
    
        if choice == "1":
            user1=create_user()
            users[user1.first_name]=user1
            time.sleep(1)
            print("user added successfuly!")
            print()
        
        
    
        elif choice == "2":
            clear()
            print("displaying all users...")
            time.sleep(2)
            if users:
                for key in users:
                    users[key].display()
            else:
                print("sorry. didint find any user to display!")
        

        
        else:
            break
    
game()

        


    
