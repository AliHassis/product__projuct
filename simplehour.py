sec=input("please enter the duration in seconds:\n")
hour= int(sec)//3600
minutes=(int(sec)%3600)//60
seconds=(int(sec)%3600)%60
print(f"the duration is : {hour} hours ,{minutes} minutes and {seconds} seconds ")