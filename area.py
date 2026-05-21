area=input("chose an area from the list: (khalil),(samou),(palestine)\n")
if area.lower()=="khalil" or area.lower()=="samou" or area.lower()=="palestine":
    print(f"{area} is on our list")
else:
    print(f"{area} is not on our list")