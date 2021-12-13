import streamlit as st
from information import information
from about import about_page
from explore import explore_dataframe
from plot import plot_data
from predict import show_predict




html_temp ="""
    <marquee width="150%" direction="right" height="50px"  bgcolor ='#D6EEEE'
     behavior =alternate   style='font=size:35px'   >
    Developed By Rohit sharma
    </marquee>


<br>

    """
st.markdown(html_temp,unsafe_allow_html=True)

    
   

st.set_option('deprecation.showPyplotGlobalUse', False)
page = st.sidebar.selectbox(" Explore  or  Predict ", ("Accuracy Table", "Explore","Plot","Predict",'About'))


if page == "Accuracy Table":
    information()
    


elif page=='Explore':
    explore_dataframe()


elif page=='Plot':
    plot_data()
    
elif page=='Predict':
    show_predict()

elif page=='About':
    about_page()



