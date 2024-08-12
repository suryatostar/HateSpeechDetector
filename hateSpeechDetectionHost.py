import streamlit as st
import joblib

model = joblib.load("./hatespeech.pkl")

st.title("Hate Speech Detection")

speech = st.text_input("Write your text here...")
if st.button("Analyse"):
    prediction = model.predict([speech])
    if prediction[0]==1:
        st.error("Hate Speech")
    elif prediction[0]==0:
        st.info("Safe Speech")
st.image("./hatespeech.jpeg",width=700)