import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np


def pca_maker(df):
    numerical_columns = []
    categorical_columns =  []

    for i in df.columns:
        if df[i].dtype == np.dtype("int64") or df[i].dtype == np.dtype("float64"):
            numerical_columns.append(df[i])
        
        else:
            categorical_columns.append(df[i])
            

    numerical_data = pd.concat(numerical_columns, axis=1)
    categorical_data = pd.concat(categorical_columns, axis=1)

    numerical_data =numerical_data.apply( lambda x: x.fillna(x.mean()))

    scaler = StandardScaler()

    scaled_values = scaler.fit_transform(numerical_data)

    scaled_values = pd.DataFrame(scaled_values)
    scaled_values

    pca = PCA()

    pca_data = pca.fit_transform(scaled_values)

    pca_data = pd.DataFrame(pca_data)


    new_columns_name =["PCA_" + str(i) for i in range(1, len(pca_data.columns) + 1)]
    new_columns_name_dic = {index: value for index, value in enumerate(new_columns_name)}

    pca_data.rename(columns=new_columns_name_dic, inplace=True)


    output =  pd.concat([df, pca_data], axis=1)

    return output, list(categorical_data.columns), new_columns_name

