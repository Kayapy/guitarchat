from dotenv import load_dotenv
import openai
import streamlit as st
import os

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Guitar Chat")

st.subheader("Guitar Riff Idea Generator")

Guitar_Riff_Idea_Generator = st.text_input("Type Here What You Want To Create on the Guitar:")

if Guitar_Riff_Idea_Generator:
    resposta = openai.Completion.create(
        model="text-davinci-003",
        prompt=Guitar_Riff_Idea_Generator,
        max_tokens=1000,
        n=1
    )
    st.subheader("RESPOSTA")
    st.write(resposta.choices[0].text)
