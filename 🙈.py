print("welcome to place the rabbit")
list=[["🌻", "🌻","🌻"],["🌻", "🌻","🌻"],["🌻", "🌻","🌻"]]

print(list[0])
print(list[1])
print(list[2])
go=input("where shoud the monky is go? 🙈\nplease choose a row and a coulmn:")

row=int(go[0])-1
coulmn=int(go[1])-1

list[row][coulmn]="🙈"


print(list[0])
print(list[1])
print(list[2])


