import streamlit as st
import pandas as pd
import seaborn as sns
st.write("This app is purely dedicated to data analyticsss")

sales = pd.read_csv(r"Sales.csv")
sales

s1 = sales.groupby('Export Class').agg(Total_Sales=("Revenue","sum"),Total_Quantity=("Quantity Sold","sum"))
s1

s2 = sns.jointplot(x = 'Revenue', y = 'Quantity Sold',data = sales)
s2
