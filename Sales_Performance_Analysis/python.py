import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

order_data=[
    {'product':'Biscuits','city':'New York', 'units':'12','price':'2',},
    {'product':'Chocolate','city':'Los Angeles', 'units':'20','price':'3'},
    {'product':'Sweets','city':'Chicago', 'units':'15','price':'1.5'},
    {'product':'Milkshake','city':'New York', 'units':None,'price':'4'},
    {'product':'Cookies','city':'Houston', 'units':'10','price':'2.5'},
    {'product':'Cake','city':'Chicago', 'units':'8','price':'6'},
    {'product':'Chocolate','city':'Los Angeles', 'units':'20','price':'3'},
    {'product':'Biscuits','city':'New York', 'units':'12','price':'2'},
]
df_order= pd.DataFrame(order_data)

df_order['units']=pd.to_numeric(df_order['units'])
print(df_order['units'])
df_order['price']=pd.to_numeric(df_order['price'])
print(df_order['price'])

df_order['total_revenue']= df_order['units'] * df_order['price']
print(df_order['total_revenue'])

print(
    df_order.groupby('product')['total_revenue'].sum()
    .sort_values(ascending=False)
    )

print(
    df_order.groupby('city')['total_revenue'].sum()
)

print(
    df_order.groupby('product')['total_revenue']
    .agg(['sum','mean','count'])
)

grouped= df_order.groupby('product')['total_revenue'].sum()
print(grouped[grouped > 40])

print(
    df_order.groupby(['product', 'city'])['total_revenue']
    .sum()
)

grouped=(
df_order.groupby('product')['total_revenue'].sum()
    .reset_index()
)
print(grouped)

product_revenue = (
    df_order.groupby("product")["total_revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(6,4))
plt.bar(product_revenue.index, product_revenue.values)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

city_revenue = df_order.groupby("city")["total_revenue"].sum()

plt.figure(figsize=(6,6))

plt.pie(
    city_revenue,
    labels=city_revenue.index,
    autopct='%1.1f%%'
)

plt.title("Revenue by City")

plt.show()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [1200, 1450, 1100, 1600, 1750, 1500]

plt.figure(figsize=(6,4))

plt.plot(months, revenue, marker='o')

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()

plt.show()

revenue = [24, 60, 22.5,None, 25, 48, 60, 24]

plt.figure(figsize=(5,4))

sns.boxplot(x=revenue)

plt.title("Boxplot of Total Revenue")

plt.show()



print(df_order["product"].mode())


#KPI
print("===== BUSINESS KPIs =====")

# KPI 1: Total Revenue
total_revenue = df_order["total_revenue"].sum()
print("\nKPI - Total Revenue:", total_revenue)

# KPI 2: Average Order Value
average_order = df_order["total_revenue"].mean()
print("\nKPI - Average Order Value:", average_order)

#KPI 3: Total Units Sold
print("\nKPI-Total Units Sold")

#KPI 4: Number Of Orders
print("\nKPI-Number of Orders")
