import streamlit as st
import openai

# Configure a API key do OpenAI
openai.api_key = "sua_api_key_aqui"

st.title("Guitar Chat")
st.subheader("Guitar Riff Idea Generator")

Guitar_Riff_Idea_Generator = st.text_input("Type Here What You Want To Create on the Guitar:")

# Verifique se há entrada do usuário e faça a chamada à API do GPT-3.5
if Guitar_Riff_Idea_Generator:
    st.subheader("Você digitou: ")
    st.write(Guitar_Riff_Idea_Generator)

    # Chame a API do GPT-3.5 para gerar a resposta
    response = openai.Completion.create(
        engine="text-davinci-002",  # Especifique o motor do GPT-3.5 (pode variar dependendo da disponibilidade)
        prompt=Guitar_Riff_Idea_Generator,
        max_tokens=100  # Limite o tamanho da resposta, se necessário
    )

    # Exiba a resposta gerada pelo modelo
    st.subheader("Resposta do GPT-3.5:")
    st.write(response.choices[0].text)

