door=input("""welcome to my island!
there are tow doors in front of you.
a red door and a blue door.
which door to you want to open?
""")
if door.lower()=="blue":
    print("oops! you chosed the corcodie door")
    print("game over")
elif door.lower()=="red":
     box=input("""great! now you are in a room.
you found three boxes: white , black , green
which box do you open\n""")
     if box.lower() =="white":
          print("oops! you pened a box filled with snakes")
     elif box.lower()=="black":
          print("oops! you pened a box filled with spider")     
     elif box.lower()=="green":
          print("congratulations! you found the treasure!")
     else:
          print("invalid choise!")
else:
     print("invalid choise!")
  
     

