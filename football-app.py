import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

'''
# Club and Nationality App

This very simple webapp allows you to select and visualize players from certain clubs and certain nationalities.
'''

DATA_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "football_data.csv")
)

@st.cache
def load_data():
    return pd.read_csv(f"file://{DATA_PATH}")

df = load_data()
clubs = st.sidebar.multiselect('Show Player for clubs?', df['Club'].unique())
nationalities = st.sidebar.multiselect('Show Player from Nationalities?', df['Nationality'].unique())

# display table for dataframe
df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities))]
st.write(df)

# display distribution plot
fig = px.scatter(df, x ='Overall', y='Age', color='Name')
st.plotly_chart(fig)
