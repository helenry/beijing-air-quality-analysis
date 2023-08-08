import streamlit as st
import pandas as pd

test = pd.read_csv('https://docs.google.com/spreadsheets/d/' + 
                   '1Iq0E9w6BKHRpiYhHXhXCxUDFBU6wm_dZ2kaXlZuSBPc' +
                   '/export?gid=1428763389&format=csv',
                   index_col=0
                  )
st.dataframe(test)
