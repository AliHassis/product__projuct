print("*****    welcome to ishop calculater   *****")
list=[]
cost2=[]
number=int(input("how many items are there in your basket today?"))
for x in range(1,(number+1)):
    item=input(f"lsts get to counting them...\nplease tell me the name of item number {x}:")
    cost=int(input(f"what is the price of {item}\n$"))
    cost2.append(cost)
    list.append(item)
entire=input("would you like to see your entire basket items?")
if entire=="yes":
    print(list)
else:
    print("ok")

cost1=input("would you like to see how much it will cost? ")
if cost1=="yes":
    print(sum(cost2))
else:
    print("ok")
