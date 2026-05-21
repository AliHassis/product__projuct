list=[["🏵","🏵","🏵"],["🏵","🏵","🏵"],["🏵","🏵","🏵"]]

print(list[0])
print(list[1]) 
print(list[2])
go=input("where shoud the rabbit go? 🙈")
go1=int(go)-1
go2=int(go)-1
go3=list[go1][go2]
list[go1].remove(go3)
list[go1].insert(go3,"🙈")
print(list)