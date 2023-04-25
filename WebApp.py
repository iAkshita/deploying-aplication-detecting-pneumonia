import streamlit as st
import numpy as np
import pandas as pd
import pickle


# pickle_in1 = open('mymodel.pkl', 'rb')
# classifier1 = pickle.load(pickle_in1)


st.header("Pneumonia Detection")
st.subheader("Enter your credentials, and upload your chest X-ray images to detect Pneumina")


st.text_input("Name: ")


st.select_slider("Gender:", ['Male', 'Others', 'Female'])


st.text_input("Email or icloud: ")


st.file_uploader("Upload your chest X-ray")


def predict():
    return st.write("Pneumonia detected")


st.button('Predict', on_click=predict)


st.text_input("write your review or symptoms for the disease ")
