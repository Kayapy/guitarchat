import streamlit as st
import openai
import os
from dotenv import load_dotenv
import toml

# Carregue as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a API key da OpenAI
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Carregue os segredos do arquivo secrets.toml
secrets = toml.load("secrets.toml")
openai_credentials = secrets.get("openai_credentials", {})
api_key = openai_credentials.get("api_key")

if not api_key:
    raise ValueError("Chave de API da OpenAI não encontrada no arquivo secrets.toml ou no arquivo .env")

# Agora você pode usar a variável api_key para configurar a API da OpenAI
openai.api_key = api_key

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

