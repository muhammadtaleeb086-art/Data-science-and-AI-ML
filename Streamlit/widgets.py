import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name")

age = st.slider("Select your age : ",0,100,25)

st.write(f"Your age is {age}.")

options = ["Python","Java","C++","JavaScript"]
choice = st.selectbox("Choose your favourite language:",options)
st.write(f"You selected {choice}.")



if name:
  st.write(f"Hello , {name}")

data = {
  "Name":["Taleeb","kaif","danish","aziz"],
  "Age":[21,22,20,40],
  "City":["New York","Los Angeles","Chicago","bihar"]
}

df = pd.DataFrame(data)
df.to_csv("data.csv")
st.write(df)

upload_files = st.file_uploader("Choose a csv file",type="csv")

if upload_files is not None:
  df=pd.read_csv(upload_files)
  st.write(df)
