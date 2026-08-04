import pandas as pd
import streamlit as st

st.title('Welcome to y_footy_analytics_v1')

st.dataframe(pd.DataFrame({
    'col1': ['a', 'b', 'c', 'd'],
    'col2': [1, 2, 3, 4]
}))