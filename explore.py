import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
from scipy.stats import skew

def explore_dataframe():

        
    
    df=pd.read_csv('abalone.csv')

    if st.sidebar.checkbox('show Dataset'):
        st.dataframe(df)

        
    if st.sidebar.checkbox('Head of Data'):
        st.dataframe(df.head())

    if st.sidebar.checkbox('feature names'):
        st.write(df.columns)


    if st.sidebar.checkbox('Tail of Data'):
        st.write(df.tail())

        

    if st.sidebar.checkbox('Summary of Data'):
        st.write(df.describe())

    if st.sidebar.checkbox('Skewness  of Each column'):
        st.write(df.skew())

    if st.sidebar.checkbox('Correlation of Data'):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()

    if st.sidebar.checkbox('Pair plot of Data'):
        st.write(sns.pairplot(df))
        st.pyplot()


    
