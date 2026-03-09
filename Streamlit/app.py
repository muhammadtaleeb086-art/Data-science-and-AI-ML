import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlit")


## Display a simple text
st.write("This is a simple text")

## Create A simple DataFrame

df = pd.DataFrame({
  'first column':[1,2,3,4],
  'second column':[10,20,30,40]
})

##Display the Dataframe 
st.write("Here is the dataframe")
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randint(0, 20, size=(20,3)),
    columns=['A','B','C']
)

st.line_chart(chart_data)