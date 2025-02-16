import streamlit as st
import pandas as pd
import matplotlib as plt

st.title("Line Plot Practice")

data = pd.DataFrame({
    "x": [5, 10, 15, 20],
    "y": [10, 20, 30, 40]})

plt.plot(df['x'], df['y'])

