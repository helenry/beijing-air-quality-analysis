import streamlit as st
import datetime
import pandas as pd

test = pd.read_csv('https://docs.google.com/spreadsheets/d/' + 
                   '1Iq0E9w6BKHRpiYhHXhXCxUDFBU6wm_dZ2kaXlZuSBPc' +
                   '/export?gid=1428763389&format=csv',
                   index_col=0
                  )
st.dataframe(test)

# Input Widget
# .text_input()
name = st.text_input(label="Nama lengkap", value="")
st.write("Nama: ", name)

# .text_area()
text = st.text_area("Feedback")
st.write("Feedback: ", text)

# .number_input()
number = st.number_input(label="Umur")
st.write("Umur: ", int(number), " tahun")

# .date_input()
date = st.date_input(label="Tanggal lahir", min_value=datetime.date(1900, 1, 1))
st.write("Tanggal lahir: ", date)

# .file_uploader()
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# .camera_input()
picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)

# Button Widget
# .button()
if st.button("Say hello"):
    st.write("Hello there")

# .checkbox()
agree = st.checkbox("I agree")
if agree:
    st.write("Welcome to MyApp")

# .radio()
genre = st.radio(
    label="What is your favorite movie genre",
    options=("Comedy", "Drama", "Documentary"),
    horizontal=False
)

# .selectbox()
genre = st.selectbox(
    label="What is your favorite movie genre",
    options=("Comedy", "Drama", "Documentary")
)

# .multiselect()
genre = st.multiselect(
    label="What is your favorite movie genre",
    options=("Comedy", "Drama", "Documentary")
)

# .slider()
values = st.slider(
    label="Select a range of values",
    min_value=0,
    max_value=100,
    value=(0, 100)
)
st.write("Values: ", values)
