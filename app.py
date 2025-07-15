import StreamLitFifa_29.eda as eda, StreamLitFifa_29.prediction as prediction
import streamlit as st

with st.sidebar:
    st.write('# Page Navigation')

    page = st.selectbox('Pilih Halaman',['EDA','Predict Rating'])

    st.write ('# About')
    st.markdown ('Page ini Berisi Tentang Hasil Analisis Data Terhadap Pemain Di FIFA 2024 \n\n dan juga prediksi rating Pemain berdasarkan atribut Yang pemain Miliki')

if page == 'EDA':
    eda.run()

if page == 'Predict Rating':
    prediction.run()