import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
def information():

    

    html_temp1 ="""
    <div style='background-color:#D6EEEE';> <p style='font=size:25px'> Abalone Age Prediction From Physical Measurement </p> </div>
    <div class="col-div-8">
		<div class="box-8">
		<div class="content-box ">
		<p style='background-color:#D6EEEE';>Machine Learning Models    and   their     Accuracy Score</p>
		<br>
		<table border='2'  style="width:100%" border-style:double; >
    <tbody  >
    <tr style="height:75px" >
    <th style='background-color:#CCFF66';>Random Forest</th>
    <th style='background-color:#CCFF66';>Random</th>
    <th style='background-color:#CCFF66';>91% </th>
    </tr>
    <tr style="height:75px">
    <th style="background-color:powderblue;">Xtreme Gradient Boosting</th>
    <th  style="background-color:powderblue;" >XtremeGradient</th>
    <th  style="background-color:powderblue;">84%</th>
    </tr>
    <tr style="height:50px">
    <th>Decision Tree</th>
    <th>DT</th>
    <th>84%</th>
    </tr style="height:75px">
    <tr style="height:75px">
    <th style="background-color:powderblue;">Gradient Boosting</th>
    <th style="background-color:powderblue;">Gradient</th>
    <th style="background-color:powderblue;"><span class="cat">73%</span></th>
    </tr>
    <tr style="height:75px">
    <th>K Nearest Neighbors</th>
    <th>KNN</th>
    <th>72%</th>
    </tr>
    <tr style="height:75px">
    <th style="background-color:powderblue;">Support Vector Machine</th>
    <th style="background-color:powderblue;">SVM</th>
    <th style="background-color:powderblue;">28%</th>
    </tr>
    <tr style="height:75px">
    <th>Logistic  Regression</th>
    <th>LR</th>
    <th>26%</th>
    </tr>
    <tr style="height:75px">
    <th style="background-color:powderblue;">ADA Boosting</th>
    <th style="background-color:powderblue;">ADA</th>
    <th style="background-color:powderblue;">13%</th>
    </tr

    
    """

    st.markdown(html_temp1,unsafe_allow_html=True)


