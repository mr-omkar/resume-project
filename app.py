import pandas as pd
import numpy as np

import streamlit as st

st.header("Projects ")
st.info("ML-DL-Pyhton Project")
a_url1 = "https://mr-omkar-mumbai-property-price-predictor-app-l7qi1t.streamlit.app/"
a_url2 = "https://mr-omkar-travel-recommender-app-h321l4.streamlit.app/"
a_url3 = "url3"

a = {
    'Projects':['Mumbai Property Price Predictor','Travel Recommender(India)','Loan Price Predictor'],
     'URL': [a_url1,a_url2,a_url3]
}

b_url1 = 'https://lookerstudio.google.com/s/knrCb-nJKGg'

b = {
    'Project':['TLC Daily taxi report'],
    'URL' : [b_url1]
}

r1 = pd.DataFrame.from_dict(a)
r2 = pd.DataFrame.from_dict(b)

st.table(r1)
st.info("Analytics")
st.table(r2)
