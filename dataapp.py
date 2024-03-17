import streamlit as st
import pandas as pd

st.write("This app is purely dedicated to data analyticsss")
st.title("Homepage")
iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)
sales = pd.read_csv(r"Sales.csv")
sales

s1 = sales.groupby('Export Class').agg(Total_Sales=("Revenue","sum"),Total_Quantity=("Quantity Sold","sum"))
s1

st.button("Re-run")
