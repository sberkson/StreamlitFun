import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# My First Streamlit Webpage

Here is a Live Update!
And then here is some more text
""")

df = pd.read_csv('data.csv')
st.dataframe(df)

options = st.selectbox('Which option do you want:', ['show plotting', 'show slider'])

if options == 'show slider':
    x = st.slider('x')
    st.write('2 * x = ', 2*x)
if st.checkbox('Show Plotting'):
    sample_df = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
    st.line_chart(sample_df)


