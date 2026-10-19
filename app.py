import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.title('Tecrübe, Yazılı ve sözlü sınava göre tahmin eden model :heavy_dollar_sign:')
model=pickle.load(open('maas.pkl','rb'))
tecrube=st.number_input('Tecrube',1,10)
yazili=st.number_input('Yazili',1,10)
mulakat=st.number_input('mulakat',1,10)
if st.button('Tahmin Et'):
    tahmin =model.predict([[tecrube,yazili,mulakat]])
    tahmin=round(tahmin[0][0],2)
    st.success(f'Maas Tahmini:{tahmin}')

    