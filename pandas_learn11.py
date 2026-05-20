import os
import numpy as np
import pandas as pd


class Product:

    def __init__(self, product_name, category, price, quantity, discount):
        self.product_name = product_name
        self.category = category
        # تحويل المدخلات إلى أرقام فوراً لضمان سلامة العمليات الحسابية
        self.price = float(price) if price else 0.0
        self.quantity = int(quantity) if quantity else 0
        self.discount = float(discount) if discount else 0.0


def get_user_input():
    print("\n" + "=" * 40)
    print("📥 enter the details of the new product: ")
    print("=" * 40)

    product_name = input("🔹 Enter the product name: ").strip()
    category = input("🔹 Enter the category: ").strip()
    price = input("🔹 Enter the price: ").strip()
    quantity = input("🔹 Enter the quantity: ").strip()
    discount = input("🔹 Enter the discount: ").strip()

    return Product(product_name, category, price, quantity, discount)


def run_system():
    file_name = "products_project.csv"

    # 1. التحقق من وجود الملف القديم أو إنشاء DataFrame جديد لحماية الكود
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        try:
            df_existing = pd.read_csv(file_name)
        except Exception:
            df_existing = pd.DataFrame()
    else:
        df_existing = pd.DataFrame()

    product_list = []

    # 2. حلقة إدخال المنتجات الجديدة من المستخدم
    if (
        input("\n❓ Would you like to add a new product? (yes/no): ")
        .lower()
        .strip()
        == "yes"
    ):
        while True:
            new_product = get_user_input()
            product_list.append(new_product.__dict__)

            if (
                input("\n❓ Did you finish adding products? (yes/no): ")
                .lower()
                .strip()
                == "yes"
            ):
                break

    # 3. دمج البيانات الجديدة مع البيانات القديمة إن وجدت
    if product_list:
        df_new = pd.DataFrame(product_list)
        if not df_existing.empty:
            data = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            data = df_new
    else:
        if df_existing.empty:
            print("⚠️ there is no data for display or orocess: ")
            return
        data = df_existing.copy()

    # 4. تنظيف وتنظيم البيانات وحساب صافي المبيعات الاستراتيجي
    data["price"] = pd.to_numeric(data["price"], errors="coerce").fillna(0.0)
    data["quantity"] = (
        pd.to_numeric(data["quantity"], errors="coerce").fillna(0).astype(int)
    )
    data["discount"] = (
        pd.to_numeric(data["discount"], errors="coerce").fillna(0.0)
    )

    # معادلة حساب صافي المبيعات الإجمالي الاحترافية
    data["final_price"] = (data["price"] * data["quantity"]) - data["discount"]

    # 5. استخراج التقارير الاستراتيجية الفورية (Groupby)
    category_sales = data.groupby("category")["final_price"].sum()

    print("\n" + "📊" * 20)
    print("📈 Strategic Sales Report by Category: ")
    print("=" * 40)
    print(category_sales.to_string())
    print("-" * 40)

    if not category_sales.empty:
        top_category = category_sales.idxmax()
        top_value = category_sales.max()
        print(
            f"🏆 The best-selling category is '{top_category}' with a total balance of: {top_value:.2f}"
        )

    
    print("\n🔍 DATA QUALITY AUDIT:")
    print(f"🔸 Unique products count: {data['product_name'].nunique()}")
    print(f"🔸 Missing values in table:\n{data.isna().sum().to_string()}")
    print(f"🔸 Duplicated rows removed automatically: {data.duplicated().sum()}")
    print("=" * 40)

    # 6. حفظ البيانات بشكل نظيف في ملف الـ CSV
    data.drop_duplicates(inplace=True)
    data.to_csv(file_name, index=False)
    print(f"💾 the data has been successfuly saved to the gile: {file_name}\n")


# تشغيل النظام تلقائياً عند تشغيل الملف
if __name__ == "__main__":
    run_system()