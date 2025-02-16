import streamlit as st
import pandas as pd
import matplotlib as plt

st.title("Line Plot Practice")

data = pd.DataFrame({
    "x": ['a', 'b', 'c', 'd'],
    "y": [10, 20, 30, 40]})

df.plot(x="x", y="y", kind='bar')
