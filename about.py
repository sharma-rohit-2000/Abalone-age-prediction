import streamlit as st
from PIL import Image

def about_page():

    html="""

    <p  style='font=size:20px'>
    The economic value of abalone is positively correlated with its age. Therefore,
    to detect the age of abalone accurately is important for both farmers and
    customers to determine its price. ... Hence, researchers are interested in
    relating abalone age to variables like length, height and weight of the animal
    </p>
    <br>
    <p  style='font=size:20px' >
    The goal of this challenge is to classify abalone snails Age according to their
    number of rings based onsome input features which are related to the abalone gender,
    as well as several length and weight measurements.</p><br>

    <p  style='font=size:20px'  >
    Abalone (from Spanish Abulón) are shellfish, a genus of gastropods. Abalone are
    known by their colorful "pearlescent" inside shell. This is also called ear-shell,
    ormer in Guernsey, abalone in South Africa, and pāua in New Zealand.
    </p>
    <br>
    <p style='font=size:20px'>Abalone attach to rocky substrates with a muscular foot, and they are manually
    removed with a blunt knife or similar implement. Owing to the slow growth rates
    and high value, most countries regulate harvesting. Size and catch limits and
    closed seasons apply in Australia, New Zealand, South Africa and the USA, although
    with variable management success.
    </p>
    <br>
    """
    st.markdown(html,unsafe_allow_html=True)
    st.image('abalonepic.jpg',caption='Ablone Shell')

    html_temp1 ="""

    <p style='font=size:25px'>Abalone Jewellery</p>

       <p  style='font=size:20px' >Abalone has been an important staple in native cultures
    around the world, specifically in Africa and on the North American West coast.
    The meat was used as food, and the shell was used as currency for many tribes.
    </p>

    <p  style='font=size:20px'>The goal of this challenge is to classify abalone snails Age according
    to their number of rings based onsome input features which are related to the abalone gender, as well as
    several length and weight measurements.</p>

    <p style='font=size:20px'>
    The dramatically high cost of abalone comes from its rarity and the difficulty experienced in obtaining it.
    It's a kind of sea snail, and each one must be gathered by hand from the ocean. The cost is also driven up
    by the label of luxury attached to it, like Wagyu beef or caviar.
    </p>

   

 

    """

    st.markdown(html_temp1,unsafe_allow_html=True)
    st.image('jewellery.jpg',caption='Ablone Shell used for Jewellery ')

    html1="""
    
    <p style='font=size:25px'>NATIVE AMERICAN CULTURES</p>
    
    <p style='font=size:20px'>
    In some Native American cultures, the shell of the abalone is to burn sage.</p>
    <p style='font=size:20px'>
    They believe the combined spiritual power of abalone and sage would take their messages to
    their Gods.
    The smoke of the sage is used to cleanse evil spirits. This is used in modern-day cleaners also,
    which we explore later.
    </p>

    <p  style='font=size:20px' >
    Smudging is a traditional cleansing ritual that has been used by Indigenous people around the
    world for centuries, and involves the burning of sacred herbs and medicines to produce a
    cleansing smoke. A smudge bowl is used to catch the ash produced during the smudging ritual,
    and to save the burned medicines to be used the next time you need to cleanse.
    </p>
    """

    st.markdown(html1,unsafe_allow_html =True)
    st.image('smoke.jpg',caption='Abalone  and Sage')


