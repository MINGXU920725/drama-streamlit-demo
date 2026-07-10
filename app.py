import streamlit as st

st.title("LLM Demo")

question = st.text_input("Question")

if st.button("Generate"):
    st.write("Hello! This is a test.")
