list=[["🏵","🏵","🏵"],["🏵","🏵","🏵"],["🏵","🏵","🏵"]]
print("welcome to place thr rabbit")
print(list[0])
print(list[1]) 
print(list[2])
go=input("where shoud the rabbit go? 🙈")


go1=int(go[0])-1
go2=int(go[1])-1

list[go1][go2]="🙈"

print(list[0])
print(list[1]) 
print(list[2])