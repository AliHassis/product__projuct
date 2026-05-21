import streamlit as st
import pandas as pd
import os

# 1. إعدادات الصفحة
st.set_page_config(page_title="Sales Dashboard Pro", page_icon="📊", layout="wide")

# 2. التنسيق العربي الكامل للمحتوى والأزرار
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;700&display=swap');
    .block-container, div[data-testid="stMetric"], div[data-testid="stSelectbox"], div[data-testid="stTextInput"], div[data-testid="stNumberInput"] {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif;
    }
    div[data-testid="stMetric"] {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        border-right: 5px solid #007bff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
    }
    div[data-testid="stTabs"] {
        direction: rtl !important;
    }
    </style>
    """, unsafe_allow_html=True)

FILE_NAME = "products_project.csv"
COLUMNS_LIST = ['product_name', 'category', 'price', 'discount_pct', 'price_after_discount', 'quantity', 'total_stock_value']

def load_data():
    if os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) > 0:
        try:
            file_df = pd.read_csv(FILE_NAME)
            file_df = file_df.reindex(columns=COLUMNS_LIST)
            file_df['price'] = pd.to_numeric(file_df['price'], errors='coerce').fillna(0.0)
            file_df['discount_pct'] = pd.to_numeric(file_df['discount_pct'], errors='coerce').fillna(0.0)
            file_df['price_after_discount'] = pd.to_numeric(file_df['price_after_discount'], errors='coerce').fillna(0.0)
            file_df['quantity'] = pd.to_numeric(file_df['quantity'], errors='coerce').fillna(1).astype(int)
            file_df['total_stock_value'] = pd.to_numeric(file_df['total_stock_value'], errors='coerce').fillna(0.0)
            return file_df
        except:
            return pd.DataFrame(columns=COLUMNS_LIST)
    else:
        return pd.DataFrame(columns=COLUMNS_LIST)

df = load_data()

# --- شريط جانبي (Sidebar) لإضافة منتج جديد ---
st.sidebar.header("➕ إضافة منتج جديد")

default_categories = ["Electronics", "Food", "Drink", "Detergents"]
if not df.empty and 'category' in df.columns:
    existing_categories = list(df['category'].dropna().unique())
    if not existing_categories:
        existing_categories = default_categories
else:
    existing_categories = default_categories

category_options = existing_categories + ["➕ إضافة قسم جديد..."]

with st.sidebar.form(key='add_product_form', clear_on_submit=True):
    new_name = st.text_input("اسم المنتج:")
    selected_cat = st.selectbox("القسم:", category_options)
    custom_category = st.text_input("إذا اخترت قسماً جديداً، اكتب اسمه هنا:")
    
    new_price = st.number_input("السعر الأصلي للقطعة ($):", min_value=0.0, value=0.0, step=1.0)
    new_discount = st.number_input("نسبة الخصم (%):", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
    new_quantity = st.number_input("الكمية المتاحة (المخزون):", min_value=1, value=1, step=1)
    
    submit_button = st.form_submit_button(label="حفظ المنتج")

if submit_button:
    if new_name.strip():
        final_category = custom_category.strip() if selected_cat == "➕ إضافة قسم جديد..." and custom_category.strip() else selected_cat
        
        discount_amount = new_price * (new_discount / 100)
        single_price_after_discount = new_price - discount_amount
        total_value = single_price_after_discount * new_quantity
        
        new_row = pd.DataFrame([{
            'product_name': new_name.strip(),
            'category': final_category,
            'price': round(new_price, 2),
            'discount_pct': round(new_discount, 2),
            'price_after_discount': round(single_price_after_discount, 2),
            'quantity': int(new_quantity),
            'total_stock_value': round(total_value, 2)
        }])
        
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(FILE_NAME, index=False)
        st.sidebar.success(f"✔️ تم إضافة {new_name} بنجاح!")
        st.rerun()
    else:
        st.sidebar.error("⚠️ يرجى إدخال اسم المنتج أولاً.")

# --- المحتوى الرئيسي للوحة التحكم ---
st.title("📊 لوحة تحكم إدارة المبيعات والمخزون الاحترافية")
st.write("نظام ذكي متكامل لعرض البيانات وتحليل المخزون المالي فورياً.")
st.markdown("---")

total_products = len(df)
total_sales_value = df['total_stock_value'].sum() if not df.empty else 0.0

col_m1, col_m2 = st.columns(2)
with col_m1:
    st.metric(label="📦 إجمالي عدد المنتجات في المستودع", value=total_products)
with col_m2:
    st.metric(label="💰 القيمة المالية الإجمالية للمخزون", value=f"${total_sales_value:,.2f}")

st.markdown("---")

# أدوات الفلترة والبحث
col_f1, col_f2 = st.columns(2)
with col_f1:
    categories_filter = ["الكل"] + list(df['category'].dropna().unique()) if not df.empty else ["الكل"]
    selected_category = st.selectbox("🔍 تصفية حسب القسم:", categories_filter)
with col_f2:
    search_query = st.text_input("📝 ابحث عن منتج بالاسم:")

df_filtered = df.copy()
if not df_filtered.empty:
    if selected_category != "الكل":
        df_filtered = df_filtered[df_filtered['category'] == selected_category]
    if search_query:
        df_filtered = df_filtered[df_filtered['product_name'].str.contains(search_query, case=False, na=False)]

st.markdown("---")

tab_table, tab_chart = st.tabs(["📋 مستودع البيانات الحالي", "📈 الرسوم والتحليلات البيانية"])

with tab_table:
    st.subheader("📋 قائمة المنتجات الحالية:")
    if not df_filtered.empty:
        display_df = df_filtered.rename(columns={
            'product_name': 'اسم المنتج', 'category': 'القسم', 'price': 'السعر الأصلي ($)',
            'discount_pct': 'نسبة الخصم (%)', 'price_after_discount': 'السعر بعد الخصم ($)',
            'quantity': 'الكمية المتاحة', 'total_stock_value': 'إجمالي قيمة المخزون ($)'
        })
        st.dataframe(display_df, use_container_width=True)
        
        # 📥 ميزة التصدير الجديدة: تحميل البيانات كملف Excel/CSV مصفى جاهز للطباعة
        csv_data = df_filtered.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="📥 تحميل التقرير الحالي كملف CSV للطباعة",
            data=csv_data,
            file_name='inventory_report.csv',
            mime='text/csv',
        )
    else:
        st.info("المستودع فارغ حالياً.")
    
    st.markdown("---")
    st.markdown("### 🗑️ إدارة وحذف المنتجات:")
    if not df_filtered.empty:
        product_to_delete = st.selectbox("اختر المنتج الذي ترغب في حذفه نهائياً:", df_filtered['product_name'].unique())
        if st.button(f"❌ حذف المنتج ({product_to_delete}) من النظام", type="primary"):
            df = df[df['product_name'] != product_to_delete]
            df.to_csv(FILE_NAME, index=False)
            st.success(f"💥 تم حذف المنتج '{product_to_delete}' بنجاح!")
            st.rerun()

with tab_chart:
    if not df_filtered.empty:
        col_chart1, col_chart2 = st.columns(2)
        with col_chart1:
            st.subheader("📈 إجمالي القيمة المالية للمخزون لكل منتج:")
            chart_data = df_filtered.set_index('product_name')['total_stock_value']
            st.bar_chart(chart_data, use_container_width=True)
            
        with col_chart2:
            st.subheader("📊 نسبة القيمة المالية لكل قسم بالمستودع:")
            # تجميع البيانات حسب القسم لإظهار الرسم التوضيحي الدائري
            category_pie = df_filtered.groupby('category')['total_stock_value'].sum()
            st.scatter_chart(category_pie, use_container_width=True)
    else:
        st.info("لا توجد بيانات كافية لعرض الرسم البياني.")