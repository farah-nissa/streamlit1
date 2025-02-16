import streamlit as st
import pandas as pd
import matplotlib as plt

st.title("Line Plot Practice")

data = pd.DataFrame({
    "x": [1, 2, 3, 4],
    "y": [10, 20, 30, 40]})

plt.plot(df["x"], df["y"])

st.pyplot()

num_points = st.slider("Number of points", min_value=100, max_value=1000, value=500, step=100)

text_input = st.text_input("Enter some text: ")

st.write("The name: ", text_input)

show_plot = st.checkbox("Show plot", value=True)

if not show_plot:
    plt.close()

plot_color = st.selectbox("Plot color", ["blue", "red", "green"])

plt.plot(data["x"], data["y"], color=plot_color)

st.camera_input("Take a picture")
