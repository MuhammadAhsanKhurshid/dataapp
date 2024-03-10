import streamlit as st
import pandas as pd

st.write("This app is purely dedicated to data analyticsss")

sales = pd.read_csv(r"Sales.csv")
sales


