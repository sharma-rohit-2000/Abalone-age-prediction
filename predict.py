import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import warnings
import pickle
warnings.filterwarnings('ignore')
from sklearn.ensemble import RandomForestClassifier
import withoutpickle

df=pd.read_csv('abalone.csv')
features=df.iloc[:,:-1]
target=df.iloc[:,-1]

def show_predict():
    

    
    
    gender=st.selectbox('Gender  (0 used for female 1 used for male)' ,(0,1))
    length =st.slider('length in mm',0.075000,1.0000)
    Diameter =st.slider('Diameter in mm',0.055000,1.0000)
    Height =st.slider('Height in mm',0.0000,1.5000)
    Whole_weight   = st.slider('Whole weight in gram',0.002000,3.0000)
    Shucked_weight = st.slider('Shucked weight in gram',0.001000,1.5000)
    Viscera_weight = st.slider('Viscera weight in gram',0.000500,0.8000)
    Shell_weight = st.slider('Shell weight in gram',0.139203,1.005000)


    data={'gender':gender,
          'length':length,"Diameter":Diameter,'Height':Height,'Whole_weight':Whole_weight,'Shucked_weight':Shucked_weight,
          'Viscera_weight':Viscera_weight,'Shell_weight':Shell_weight}
    features=pd.DataFrame(data,index=[1])

    st.write(features)

    
    
    prediction=withoutpickle.show(features)


    st.subheader('Prediction')

    df1=pd.DataFrame(prediction,index=['Prediction of our model'],columns=['Age'])
    
    st.dataframe(df1)
   
    

  


    

    

