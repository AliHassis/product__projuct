import pandas as pd
import numpy as np

class sail:
    def __init__(self, product_name, category, price, quantity, discount):
        self.product_name=product_name
        self.category=category
        self.price=price
        self.quantity=quantity
        self.discount=discount


def user():
    product_name=input("enter the productname: ")
    category=input("enter the category: ")
    price=(input("enter the price: "))
    quantity=(input("enter the quantity: "))
    discount=(input("enter the discount: "))

    return sail(product_name, category, price, quantity, discount)


dic={}
fun={}

while True:
    user1=user()
    dic[user1.product_name]=user1
    if input("finish? : ") == "y":
        break

clean_data={id:vars(obj) for id , obj in dic.items()}
df=pd.DataFrame.from_dict(clean_data, orient="index")

df=df.replace("", np.nan)
df["price"]=pd.to_numeric(df["price"], errors="coerce")
df["quantity"]=pd.to_numeric(df["quantity"], errors="coerce")
df["discount"]=pd.to_numeric(df["discount"], errors="coerce")
df["price"] = df["price"].fillna(0)
df["quantity"] = df["quantity"].fillna(0)
df["discount"] = df["discount"].fillna(0)


df["category"] = df["category"].fillna("unknown")
df.loc[df["price"]==0, "price"] = 1

def price_5(plus):
    return plus + 5
df["price"]=df["price"].apply(price_5)

df["final_price"]=(df["price"]*df["quantity"])-df["discount"]

df=df.sort_values(by="price")

while True:
    user2=user()
    fun[user2.product_name]=user2
    if input("finish? : ") == "y":
        break

clean_data={id:vars(obj) for id , obj in fun.items()}
fd=pd.DataFrame.from_dict(clean_data, orient="index")

fd=fd.replace("", np.nan)
fd["price"]=pd.to_numeric(df["price"], errors="coerce")
fd["quantity"]=pd.to_numeric(fd["quantity"], errors="coerce")
fd["discount"]=pd.to_numeric(fd["discount"], errors="coerce")
fd["price"] = fd["price"].fillna(0)
fd["quantity"] = fd["quantity"].fillna(0)
fd["discount"] = fd["discount"].fillna(0)


fd["category"] = fd["category"].fillna("unknown")
fd.loc[fd["price"]==0, "price"] = 1

def price_5(plus):
    return plus + 5
fd["price"]=fd["price"].apply(price_5)


fd["final_price"]=(fd["price"]*fd["quantity"])-fd["discount"]

fd=fd.sort_values(by="price")

data=pd.concat([df,fd])
print(data)
print(data["product_name"].unique())


