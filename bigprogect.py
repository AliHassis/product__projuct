import os
import time
import pandas as pd


def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

class gym:
    def __init__(self, first_name, last_name, membership, status):
        self.first_name=first_name
        self.last_name=last_name
        self.membership=membership
        self.status=status

    def display(self):
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")
        print(f"membership: {self.membership}")
        print(f"membership status: {self.status}")
        print("__________________________")
    
def create_user():
    first_name=input(f"enter first name: ")
    last_name=input(f"enter last name: ")
    membership=input(f"enter membership: ")
    status=input(f"enter membership status, or click enter: ")
    if status:
        pass
    else:
        status="inactive"    

    return gym(first_name, last_name, membership, status)



fun={}

def start():
    while True:
        print("welcome to gym membership management")
        print()
        choice=input("""choose an action:\n
1. add new member 
2. display all member
3. search for a member
4. exit\n                            
enter your choice: """)
        if choice == "1":
            clear()
            user1=create_user()
            fun[user1.first_name]=user1
            print("member added successfuly!")
            time.sleep(2)
            clear()
        
        elif choice == "2":
            clear()
            if fun:
                print("displaying all members ....")
                clean_data={id:vars(obj) for id , obj in fun.items()}
                df = pd.DataFrame.from_dict(clean_data, orient="index")
                
                print(df)
                df.to_csv("gym_members.csv")
                input("enter to back")
              
                
            else:
                print("sorry. didint find any user to display!")
            time.sleep(5)
            clear()

        elif choice == "3":
            clear()
            choice1=input("""search by:\n
1. membershi id
2. first name
3. membership staus\n
enter your choice: """)
            if choice1 == "1":
                id=input("enter the membership id to search: ")
                clear()
                found = False
                for key in fun:
                    if fun[key].membership==id:
                        fun[key].display()
                        found= True
                        break
                if not found:
                        print("sorry")
                input("\nenter for back")
                clear()
            
            elif choice1 == "2": 
                name=input("enter the first name to search: ")   
                clear()
                if name in fun:
                    fun[name].display()
                else:
                    print("sorry")
                time.sleep(2)
                clear()

            elif choice == "3":
                status1=input("enter the membership status to search (active/inactive): ")
                clear()
                found= False
                for key in fun:
                    if fun[key].status == status1:
                        fun[key].display()
                        found = True
                if not found:
                    print("sorry")
                time.sleep(2)
                clear()

        elif choice == "4":
            break

        else:
            print("invaild choice! please try again.")
            time.sleep(2)
start()

