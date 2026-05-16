import pandas as pd
import numpy as np


df=pd.read_csv("products_project.csv")

class product:
    def __init__(self, product_name, category, price, quantity, discount):
        self.product_name=product_name
        self.category=category
        self.price=price
        self.quantity=quantity
        self.discount=discount



def user():
    product_name=input("enter the product name: ")
    category=input("enter the category: ")
    price=input("enter the price: ")
    quantity=input("enter the quantity: ")
    discount=input("enter the discount: ")

    return product(product_name, category, price, quantity, discount)

fun={}

def run():
    print(df)
    print("_" * 50)
    print("")
    if (input ("would you like to add new product? ")).lower() == "yes":
        while True:
            print("")
            user1=user()
            fun[user1.product_name]=user1
            if (input("have you finished? ")).lower() == "yes":
                break
    

    clean_data={id:vars(obj) for id , obj in fun.items() }
    df2=pd.DataFrame.from_dict(clean_data, orient="index")
    df2=df2.reset_index(drop=True)
        
    data=pd.concat([df,df2], ignore_index=True).copy()

    data=data.replace("", np.nan)
    data["price"]=pd.to_numeric(data["price"], errors="coerce")
    data["quantity"]=pd.to_numeric(data["quantity"], errors="coerce")
    data["discount"]=pd.to_numeric(data["discount"], errors="coerce")
        
    data["final_price"]=(data["price"] * data["quantity"]) - data["discount"]

    category_sales=data.groupby("category")["final_price"].sum()
    top_category= category_sales.idxmax()
    top_value= category_sales.max()
    print(data)
    print("_" * 20)
    print(data["product_name"].unique())
    print()
    print(data.isna().sum())
    print()
    print(data.duplicated())
    print("")
    print(f"the best-selling {top_category} with a balance of {top_value}")
    data.to_csv("products_project.csv" , index=False)
        
   

    

run()





