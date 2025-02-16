import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Line Plot Practice")

fig, df = plt.subplots()
df.plot = ([5, 10, 15, 20], [10, 20, 30, 40])

plt.plot(y, color='black')

plt.xlim(0, 40)
plt.ylim(0,40)

st.pyplot(fig)
plt.show()
