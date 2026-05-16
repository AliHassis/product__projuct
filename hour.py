str_seconds=input("pleese enter the seconds:\n")
int_seconds=int(str_seconds)
hour=int_seconds//3600
hour1=int_seconds%3600
minutes=hour1//60
minutes1=hour1%60
seconds=minutes1
str_hour=str(hour)
str_minutes=str(minutes)
str_seconds=str(seconds)
print("the course is:" +str_hour + " hours and "+ str_minutes+ " minutes and " + str_seconds + "second")