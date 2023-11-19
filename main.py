from ui import SQLAGENT

import streamlit as st


st.title("AtliQ T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = SQLAGENT()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)