tasks=input("enter your tasks for today separated by a comma:").split(", ")
done=[]
nodone=[]
for x in tasks:
    print(f"\n{x}\n ")
    yes_no=input(f"did you finish {x} already?")
    if yes_no=="yes":
        done.append(x)
        print("nice job")
    else:
        nodone.append(x)
        print("try not to put it off")
    print("--------")
no_yes=input("did you want to see your today is progress?(yes/no)")
if no_yes=="yes":
    print("     ***** done tasks *****")
    print(done)
    print("     ***** ongoing tasks *****")
    print(nodone)
else:
    print("ok")