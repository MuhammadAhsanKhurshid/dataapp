import streamlit as st
import pandas as pd


st.set_page_config(layout ='wide', initial_sidebar_state='expanded')

st.sidebar.header('Data Dashboard')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min','temp_max'))

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data',('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data',['Price','Quantity'],['Price','Quantity'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)



st.sidebar.markdown('''
---
                    Created with code by Spark ''')




st.write("This app is purely dedicated to data analyticsss")
st.title("Homepage")
iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)
sales = pd.read_csv(r"Sales.csv")
sales

s1 = sales.groupby('Export Class').agg(Total_Sales=("Revenue","sum"),Total_Quantity=("Quantity Sold","sum"))
s1

st.button("Re-run")
