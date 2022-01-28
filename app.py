from contextlib import nullcontext
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pickle


st.title("Covid-19 Dashbord")

data = pickle.load(open("sorted_df.pkl", 'rb'))

st.write(data)



select = st.selectbox("All countrys ", data['country_region'])



selected_country = data[data['country_region'] == select]


select_status = st.sidebar.radio("Status", ('Confirmed',
'Active', 'Recovered', 'Death'))




def selected_name(select):
    data_death = data[data['deaths'] == select]
    data_cases = data[data['confirmed'] == select]
    data_recorved = data[data['recovered'] == select]

    return data_death,data_cases,data_recorved

data_death,data_cases,data_recorved = selected_name(select)



# col1 , col2 , col3  = st.columns(3)

# with col1:
#     st.write(data_death)

# with col2:
#     st.write(data_cases)

# with col3:
#     st.write(data_recorved)





