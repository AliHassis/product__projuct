book=input("enter the name of a book you won:").lower()
list_book=[book]
book2=input("enter the name of another book you own (or press 'enter' to skip ):").lower()
if book2:
    list_book.append(book2)
    print(f"your libary : {list_book}")
else:
    print(f"your libary : {list_book}")    

book3=input("enter the name of a book you wish to have in the future :").lower()
wishlist=[book3]
book4=input("enter the name of a nother book you wish to have in the future : (or press 'enter' to skip)").lower()
if book4:
    wishlist.append(book4)
    print(f"your wishlist: {wishlist}")
else:
    print(f"your wishlist {wishlist}")    
    
got=input("enter the name of a book from your wishlist that yu have got it  (or press 'enter' to skip)").lower()
if got in wishlist:
    list_book.append(got)
    wishlist.remove(got)
    print(f"update libary :{list_book} ")
    print(f"update wishlist: {wishlist}")
else:
    print(f"your libary : {list_book}")
    print(f"your wishlist: {wishlist}")

donate=input("enter the nale of a book from your libary you wish to donate it (or press 'enter' to skip) ").lower()
if donate in list_book:
    list_book.remove(donate)
    print(f"final libary after donations : {list_book}")
else:
    print(f"final libary after donations : {list_book}")