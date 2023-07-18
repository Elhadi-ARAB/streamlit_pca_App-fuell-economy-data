import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
from app_function import pca_maker


st.set_page_config(layout='wide')

scatter_column, settings_column = st.columns([4, 1])

scatter_column.subheader("Multi dimensional Analysis")

settings_column.subheader("Settings")


uploaded_file = settings_column.file_uploader("Analyse Your Csv file")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    pca_data, cat_cols, pca_cols = pca_maker(df)


    categorical_variable = settings_column.selectbox("Variable Select", options = cat_cols)
    categorical_variable_2 = settings_column.selectbox("Second Variable Select", options = cat_cols)

    

    pca_1 = settings_column.selectbox("First Principle Component", options=pca_cols)
    pca_2 = settings_column.selectbox("Second Principle Component", options=pca_cols)

    scatter_column.plotly_chart(px.scatter(data_frame= pca_data, x= pca_1, y= pca_2, color=categorical_variable, hover_data= [categorical_variable_2] ,height=500, template="simple_white"), use_container_width=True)

else:
    scatter_column.subheader("Please choose your csv file")


