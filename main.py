import streamlit as st
import openai

st.title("Guitar Chat")
st.subheader("Guitar Riff Idea Generator")

Guitar_Riff_Idea_Generator = st.text_input("Type Here What You Want To Create on the Guitar:")

# Chame a API do GPT-3.5 para gerar a resposta
if Guitar_Riff_Idea_Generator:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=Guitar_Riff_Idea_Generator,
        max_tokens=100
    )

    # Verifique se a resposta gerada pelo modelo é válida
    if response.choices and response.choices[0].text.strip():
        # Exiba a resposta gerada pelo modelo
        st.subheader("Resposta:")
        st.write(response.choices[0].text)
    else:
        st.subheader("O modelo não retornou uma resposta válida.")
