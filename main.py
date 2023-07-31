import streamlit as st

st.title("Guitar Chat")
st.subheader("Guitar Riff Idea Generator")

Guitar_Riff_Idea_Generator = st.text_input("Type Here What You Want To Create on the Guitar:")

# Resto do código do seu aplicativo Streamlit
if Guitar_Riff_Idea_Generator:
    st.subheader("Você digitou: ")
    st.write(Guitar_Riff_Idea_Generator)
git submodule add https://github.com/Kayapy/guitarchat.git guitarchat2
