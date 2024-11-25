import streamlit as st
import google.generativeai as ai

ai.configure(api_key="API_KEY")

llm = ai.GenerativeModel("gemini-1.5-flash-latest")

chatbot = llm.start_chat(history=[])

st.title("Welcome to the Chatbot")

st.chat_message("ai").write("Hi there I am a helpful AI Assistant. How can I help you today?")

human_prompt = st.chat_input("Say Something...")

if human_prompt:
    st.chat_message("human").write(human_prompt)
    response = chatbot.send_message(human_prompt)
    st.chat_message("ai").write(response.text)