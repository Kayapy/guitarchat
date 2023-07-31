import openai
import streamlit as st
import toml

# Carregar as informações sensíveis do arquivo secrets.toml
secrets = toml.load("secrets.toml")

# Configurar a API key da OpenAI
openai.api_key = secrets["openai_credentials"]["api_key"]

# Resto do código do seu aplicativo Streamlit
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
