import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Configurações do tema
st.set_page_config(
    page_title="Guitar Chat",
    page_icon="🎸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Definir cores do tema
st.markdown(
    """
    <style>
    body {
        color: #3adc0d;
        background-color: #f1f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Definir fonte do texto
st.markdown(
    """
    <style>
    body {
        font-family: monospace;
    }
    </style>
    """,
    unsafe_allow_html=True
)

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Guitar Chat")
st.subheader("Guitar Riff Idea Generator")

guitar_riff_idea_generator = st.text_input("Type Here What You Want To Create on the Guitar:")

# Chame a API do GPT-3.5 para gerar a resposta
if guitar_riff_idea_generator:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=guitar_riff_idea_generator,
        max_tokens=1000,
        temperature=1.5
    )

    # Verifique se a resposta gerada pelo modelo é válida
    if response.choices and response.choices[0].text.strip():
        # Exiba a resposta gerada pelo modelo
        st.subheader("Resposta:")
        st.write(response.choices[0].text)
    else:
        st.subheader("O modelo não retornou uma resposta válida.")

