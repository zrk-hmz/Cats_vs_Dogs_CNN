import streamlit as st
import tensorflow
import requests
import numpy as np
from PIL import Image
from io import BytesIO
import os
import cv2

from keras.models import load_model
from keras.applications import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from keras import layers, models


def cnn():
        with col7:
                css =   '''<style>
                                [data-testid='stHorizontalBlock']+[data-testid='stHorizontalBlock']+[data-testid='stHorizontalBlock']>div {
                                        height: 17rem;
                                }
                                [data-testid="stVerticalBlock"] .css-ocqkz7 + .css-ocqkz7 + .css-ocqkz7 > .css-1yycg8b {
                                        height: 17rem;
                                }
                                [data-testid="stVerticalBlock"] .css-ocqkz7 + .css-ocqkz7 + .css-ocqkz7 > .css-fplge5
                                > div > div > .e1tzin5v3 + .e1tzin5v3 > div > .etr89bj2 > div { margin: auto;}
                        </style>'''
                st.markdown(css, unsafe_allow_html=True)

                if x==1:
                        st.image(image)
                        css =   '''<style>
                                        [data-testid='stFileUploader'] section {
                                                display: none;
                                        }
                                </style>'''
                        st.markdown(css, unsafe_allow_html=True)
        
        with st.container():
                st.markdown( """<style>.big-font {font-size:200px;margin:-3rem; text-align: center;!important;}</style>""",
                                       unsafe_allow_html=True)
                #st.write(type(image))
                image_np = image.resize(img_shape)
                image_np = np.array(image_np)                
                image_np = np.expand_dims(image_np, axis=0)
                image_np = preprocess_input(image_np)
                prediction = model_T.predict(image_np)
                if prediction < 0.6: st.markdown('<p class="big-font">🐱</p>', unsafe_allow_html=True)
                elif prediction > 0.6: st.markdown('<p class="big-font">🐶</p>', unsafe_allow_html=True)                
                else: st.markdown('<p class="big-font">😵‍💫</p>', unsafe_allow_html=True)

css ='''<style>p {color: black;font-weight: 600;}</style>'''
st.markdown(css, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
        st.markdown( """<style>.header {font-size:35px; font-weight:bolder; !important;}</style>""",
                unsafe_allow_html=True)
        st.markdown('<h class="header">🐱 Cats vs Dogs 🐶</h>', unsafe_allow_html=True)

col4, col5, col6= st.columns([1, 1, 1])
with col4:
        model_path= st.text_input("📂 Enter Model Path")
        if model_path:
                if os.path.isfile(model_path):
                        model_T = load_model(model_path)
                        img_shape = model_T.layers[0].input_shape[1:3]
                        img_shape = img_shape[::-1]
                else:
                        st.warning("Invalid file path. Please enter a valid path.")
with col5:
        image_file= st.file_uploader("🎴 Upload image",
                                type=["jpg", "jpeg", "png"] ,
                                accept_multiple_files=False)
        css =   '''<style>
                        [data-testid='stFileUploader'] {
                                width: 140px;
                        }
                        [data-testid='stFileUploader'] section {
                                float: left;
                        }
                        [data-testid='stFileUploader'] section > div > div > span{
                                display: none;
                        }
                        [data-testid='stFileUploader'] section > div > div > small{
                                display: none;
                        }
                        [data-testid='stFileUploader'] section {
                                padding-left: 1rem;
                                padding-right: 9.6rem;
                                padding-top: 0.3rem;
                                padding-bottom: 0.4rem;
                        }
                        [data-testid='stFileUploader'] section > button{
                                display: none;
                        }
                        [data-testid='stFileUploader'] section {
                                line-height: 1.8;
                        }
                        [data-testid='stFileUploader'] section + div {
                                float: right;
                                padding-top: 0;
                        }
                        [data-testid="stHorizontalBlock"]+[data-testid="stHorizontalBlock"]>div+div>div>div>div>div>div>ul {
                                margin-right: -5rem;
                        }
                </style>'''
        st.markdown(css, unsafe_allow_html=True)
        if image_file is not None:
                css =   '''<style>
                                        [data-testid="stFileUploader"]>section{
                                                display: none;
                                        }
                                        [data-testid="stHorizontalBlock"]+[data-testid="stHorizontalBlock"]>div+div+div>div>div>div>div>div>div{
                                                display: none;
                                        }
                        </style>'''
                st.markdown(css, unsafe_allow_html=True)
                image = Image.open(image_file)
        else:
                css =   '''<style>
                                        [data-testid="stFileUploader"]>section{
                                                display: flex;
                                        }
                        </style>'''
                st.markdown(css, unsafe_allow_html=True)
                x=0
        
with col6:
        image_url = st.empty()
        url_input = image_url.text_input("🔗 Enter url", key="1",value="")

        submit_url = st.button("Submit")
        delete_url = st.button('X')
        css =  '''<style>
                        [data-baseweb="base-input"] input {
                                line-height: 1.8;
                        }
                        [data-testid="stHorizontalBlock"]+[data-testid="stHorizontalBlock"]>
                        [data-testid="column"]+[data-testid="column"]+[data-testid="column"]
                        >div>div>div+div{
                                margin-top: -102px;
                                margin-left: 110px;
                                z-index: 1;
                                
                        }
                        [data-testid="stHorizontalBlock"]+[data-testid="stHorizontalBlock"]>
                        [data-testid="column"]+[data-testid="column"]+[data-testid="column"]
                        >div>div>div+div+div{
                                margin-top: -55px;
                                margin-left: 190px;
                        }
                        [data-testid="stHorizontalBlock"]+[data-testid="stHorizontalBlock"]>
                        [data-testid="column"]+[data-testid="column"]+[data-testid="column"]>
                        div>div>div+div>div>button{
                                background-color: green;
                        }
                        [data-testid="stHorizontalBlock"]+[data-testid="stHorizontalBlock"]>
                        [data-testid="column"]+[data-testid="column"]+[data-testid="column"]>
                        div>div>div+div+div>div>button{
                                background-color: red;
                        }
                        </style>'''
        st.markdown(css, unsafe_allow_html=True)

col7, col8= st.columns([3, 2])
           
with col8:
        if submit_url:
                if image_file is not None:
                        x=1
                        cnn()
                if url_input != "":
                        img_data = requests.get(url_input).content
                        image = Image.open(BytesIO(img_data))
                        x=1
                        cnn()
                
        else:
                x=0
        if delete_url:
                image_url.text_input("🔗 Enter url", key="2",value="")