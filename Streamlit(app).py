import streamlit as st
import time as t

# Add a picture
st.image("datavisualization.jpg")
# Title
st.title("Welcome to my app")

# Header
st.header("Visualization")

# Sub header
st.subheader("A Visual Approach to Data Analysis")

# To give information
st.info("Information details of the project")

# Warning message
st.warning("Read everything carefully or you might not understand")

# Write function
st.write("About something")
st.write(range(50))

# Error message
st.error("Wrong password")

# Succes message
st.success("Congrats! You passed!")

#Markdown1
st.markdown("Visualize")
#Markdown2 --> make the font bigger by using "#". If you use more than 1 "#", the font gets smaller
st.markdown("# Visualize")
st.markdown("## Visualize")
st.markdown("### Visualize")
st.markdown(":moon") # Emoji

st.text("Learn to visualize")

# To write a caption
st.caption(" Caption is here")

# To display a mathematical equation
st.latex(r''' a+b x^2''')

# Widgets

# Check box
st.checkbox('Login')

# Button
st.button("Click")

# Radio widget
st.radio("Pick your gender", ["Male", "Female", "Other"])

# # Select box
st.selectbox("Pick your course", ["Excel", "SQL", "Python"])

# Multiselect
st.multiselect("Choose the department", [" Sales", "Marketing", "Content"])

# Selectslider
st.select_slider("Rating", ["Bad", "Good", "Excellent", "Outstanding"])

# Slider
st.slider("Enter your number", 0, 100)

# Number_input
st.number_input("Pick a number", 0, 100)

# Text input
st.text_input("Enter your email")

# Date input
st.date_input("Opening ceremony")

# Time input
st.time_input("Hey whats the time")

# Text area
st.text_area("Welcome to the Visualization website")

# Upload a file
st.file_uploader("Upload your file")

# Choose color
st.color_picker("Color")

st.progress(90)

# Spinner function = the temporary waiting time
with st.spinner("Just wait"):
    t.sleep(2) # 2 sec loading time

# Balloons for celebration
st.balloons()

# Create a side bar to the left
st.sidebar.title("Visual studio") # Use title
st.sidebar.text("Mail address") # Use text
st.sidebar.text("Password")
st.sidebar.button("Submit") # Use button
st.sidebar.radio("Professional Expert", ["Student","Working", "Expert"])

# Data visualization
import pandas as pd
import numpy as np

# Create a bar chart
st.title("Bar Chart")
data = pd.DataFrame(np.random.rand(50, 2), columns=["x", "y"])
st.bar_chart(data)

# Line chart
st.title("Line Chart")
st.line_chart(data)

# Area chart
st.title("Area Chart")
st.area_chart(data)











