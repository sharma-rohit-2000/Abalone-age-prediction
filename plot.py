import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def  plot_data():

    df=pd.read_csv('abalone.csv')

        


    if st.sidebar.checkbox('scatter plot'):
        if st.checkbox('Height and Rings'):
            st.write(plt.scatter(data=df,x='Height',y='Rings'))
            plt.xlabel('Height')
            plt.ylabel('Rings')
            plt.grid()
            st.pyplot()

        if st.checkbox('Length and Rings'):
            st.write(plt.scatter(data=df,x='Length',y='Rings'))
            plt.xlabel('Length')
            plt.ylabel('Rings')
            plt.grid()
            st.pyplot()


        if st.checkbox('Diameter and Rings'):
            st.write(plt.scatter(data=df,x='Diameter',y='Rings'))
            plt.xlabel('Diameter')
            plt.ylabel('Rings')
            plt.grid()
            st.pyplot()

        if st.checkbox('Whole weight and Rings'):
            st.write(plt.scatter(data=df,x='Whole weight',y='Rings'))
            plt.xlabel('Whole weight')
            plt.ylabel('Rings')
            plt.grid()
            st.pyplot()

        if st.checkbox('Shell weight and Rings'):
            st.write(plt.scatter(data=df,x='Shell weight',y='Rings'))
            plt.xlabel('Shell weight')
            plt.ylabel('Rings')
            plt.grid()
            st.pyplot()

        if st.checkbox('Shucked weight and Rings'):
            st.write(plt.scatter(data=df,x='Shucked weight',y='Rings'))
            plt.xlabel('Shucked weight')
            plt.ylabel('Rings')
            plt.grid()
            st.pyplot()

        if st.checkbox('Viscera weight and Rings'):
            st.write(plt.scatter(data=df,x='Viscera weight',y='Rings'))
            plt.xlabel('Viscera weight')
            plt.ylabel('Rings')
            plt.grid()
            st.pyplot()


    if st.sidebar.checkbox('Box plot'):
        st.write(sns.boxplot(data=df))
        plt.xticks(rotation=90)
        st.pyplot()
        


        if st.checkbox('Length'):
            st.write(sns.boxplot(data=df,y='Length',x='Rings'))
            plt.xticks(rotation=90)
            st.pyplot()

        if st.checkbox('Diameter'):
            st.write(sns.boxplot(data=df,y='Diameter',x='Rings'))
            plt.xticks(rotation=90)
            st.pyplot()

            
        if st.checkbox('Height'):
            st.write(sns.boxplot(data=df,y='Height',x='Rings'))
            plt.xticks(rotation=90)
            st.pyplot()

            
        if st.checkbox('Whole weight'):
            st.write(sns.boxplot(data=df,y='Whole weight',x='Rings'))
            plt.xticks(rotation=90)
            st.pyplot()

            
        if st.checkbox('Shucked weight'):
            st.write(sns.boxplot(data=df,y='Shucked weight',x='Rings'))
            plt.xticks(rotation=90)
            st.pyplot()

            
        if st.checkbox('Viscera weight'):
            st.write(sns.boxplot(data=df,y='Viscera weight',x='Rings'))
            plt.xticks(rotation=90)
            st.pyplot()

            
        if st.checkbox('Shell weight'):
            st.write(sns.boxplot(data=df,y='Shell weight',x='Rings'))
            plt.xticks(rotation=90)
            st.pyplot()


    if st.sidebar.checkbox('Histogram Plot'):
        plt.figure(figsize=(15,12))
        all_columns = df.columns.to_list()
        column_to_plot = st.selectbox("Select 1 Column",all_columns,key='d')
        hist_plot = sns.distplot(df[column_to_plot].value_counts())
        st.write(hist_plot)
        st.pyplot()


    if st.sidebar.checkbox("Bar Plot"):
        plt.figure(figsize=(18,12))
        all_columns = df.columns.to_list()
        column_to_plot = st.selectbox("Select 1 Column",all_columns,key='b')
        bar_plot = df[column_to_plot].value_counts().plot.bar()
        plt.xticks(rotation=90)
        st.write(bar_plot)
        st.pyplot()


    if st.sidebar.checkbox("Line Plot"):
        all_columns = df.columns.to_list()
        column_to_plot = st.selectbox("Select 1 Column",all_columns,key='c')
        line_plot = df[column_to_plot].value_counts().plot.line()
        st.write(line_plot)
        plt.grid(True)
        st.pyplot()


    if st.sidebar.checkbox("Pie Plot"):
        plt.figure(figsize=(18,12))
        all_columns = df.columns.to_list()
        column_to_plot = st.selectbox("Select 1 Column",all_columns,key='a')
        pie_plot = df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
        st.write(pie_plot)
        st.pyplot()
    
