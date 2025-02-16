import streamlit as st
import pandas as pd

st.title("Income by Year")

data = pd.read_csv('C:\\\\Coding\\\\income_by_year.csv')
                     
filter_value = st.sidebar.slider("Filter Data by Value", min_value=0, max_value=100)
                     
filtered_data = data[data['income'] > filter_value]
                     
st.bar_chart(filtered_data['income'])
