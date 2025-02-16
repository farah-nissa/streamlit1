import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Line Plot Practice")

df = pd.DataFrame({
    "x": [5, 10, 15, 20],
    "y": [10, 20, 30, 40]})

plt.plot(df['x'], df['y'])
st.pyplot()

fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [1, 2, 3])

st.pyplot(fig)
