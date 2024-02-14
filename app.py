import streamlit as st
import numpy as np
from PIL import Image

# messages = ["",
#             "come on, I'll give you a hug", 
#             "fine, how about a kiss too?", 
#             "I'll throw in a massage", 
#             "how about a special message... :3", 
#             "ok, I know what you really want. Dinner's on me",
#             "think about the last one some more!",
#             "FINE. Dinner AND dessert are on me"
#             ]


st.markdown("""
    <style>
        .title {
            font-size: 64px;
            font-weight: bold;
        }
        .large-text {
            font-size: 32px;
        }
    </style>
""", unsafe_allow_html=True)

button_style = """
        <style>
        .stButton > button {
            width: 200px;
            height: 100px;
            font-size: 50px;
            font-weight: bold;
        }
        </style>
        """
st.markdown(button_style, unsafe_allow_html=True)

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage < 8:
    st.markdown("<p class='title'>Wanna be my Valentine?</p>", unsafe_allow_html=True)

if st.session_state.stage == 0:

    image = "assets/happy.png"
    st.image(image, use_column_width=True)
    col1, col2 = st.columns(2)
    with col1: st.button('Yes', on_click=set_state, args=[8])
    with col2: 
        if st.button('No', on_click=set_state, args=[1]): st.markdown("<p class='large-text'>Come on, I'll give you a hug</p>", unsafe_allow_html=True)

if st.session_state.stage == 1:
    image = "assets/stressed1.png"
    st.image(image, use_column_width=True, width=0.8)
    col1, col2 = st.columns(2)
    with col1: st.button('Yes', on_click=set_state, args=[8])
    with col2:
        if st.button('No', on_click=set_state, args=[2]): st.markdown("<p class='large-text'>Come on, I'll give you a hug!</p>", unsafe_allow_html=True)

if st.session_state.stage == 2:
    image = "assets/stressed1.png"
    st.image(image, use_column_width=True, width=0.8)
    col1, col2 = st.columns(2)
    with col1: st.button('Yes', on_click=set_state, args=[8])
    with col2:
        if st.button('No', on_click=set_state, args=[3]): st.markdown("<p class='large-text'>Fine, how about a kiss too?</p>", unsafe_allow_html=True)

if st.session_state.stage == 3:
    image = "assets/stressed2.png"
    st.image(image, use_column_width=True, width=0.8)
    col1, col2 = st.columns(2)
    with col1: st.button('Yes', on_click=set_state, args=[8])
    with col2:
        if st.button('No', on_click=set_state, args=[4]): st.markdown("<p class='large-text'>I'll throw in a massage.</p>", unsafe_allow_html=True)

if st.session_state.stage == 4:
    image = "assets/resolution.png"
    st.image(image, use_column_width=True, width=0.8)
    col1, col2 = st.columns(2)
    with col1: st.button('Yes', on_click=set_state, args=[8])
    with col2:
        if st.button('No', on_click=set_state, args=[5]): st.markdown("<p class='large-text'>How about a special massage :3</p>", unsafe_allow_html=True)

if st.session_state.stage == 5:
    image = "assets/stressed3.png"
    st.image(image, use_column_width=True, width=0.8)
    col1, col2 = st.columns(2)
    with col1: st.button('Yes', on_click=set_state, args=[8])
    with col2:
        if st.button('No', on_click=set_state, args=[6]): st.markdown("<p class='large-text'>Okay, I know what you really want. Dinner's on me.</p>", unsafe_allow_html=True)

if st.session_state.stage == 6:
    image = "assets/stressed3.png"
    st.image(image, use_column_width=True, width=0.8)
    col1, col2 = st.columns(2)
    with col1: st.button('Yes', on_click=set_state, args=[8])
    with col2:
        if st.button('No', on_click=set_state, args=[7]): st.markdown("<p class='large-text'>Come on, think about the last one some more!</p>", unsafe_allow_html=True)

if st.session_state.stage == 7:
    image = "assets/resolution.png"
    st.image(image, use_column_width=True, width=0.8)
    col1, col2 = st.columns(2)
    with col1: st.button('Yes', on_click=set_state, args=[8])
    with col2:
        st.button('YES!!', on_click=set_state, args=[8])
        st.markdown("<p class='large-text'>FINE. Dinner and dessert are both on me if you accept.</p>", unsafe_allow_html=True)

# HE SAID YES!!
if st.session_state.stage >= 8:
    image = "assets/muah.png"
    st.image(image, use_column_width=True, width=0.8)
    st.balloons()
    st.markdown("<p class='title'>I LOVE LOVE LOVEEEE UUUUUU</p>", unsafe_allow_html=True)
    


