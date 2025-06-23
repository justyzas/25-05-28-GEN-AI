import streamlit as st
from chatbot import call_llm

st.header("Local Chatbot")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Get user input
user_input = st.chat_input("Say something...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})
    response = call_llm(st.session_state.messages)

    chatbot_message = response.choices[0].message.content

    # Generate and display assistant response
    with st.chat_message("assistant"):
        st.markdown(chatbot_message)

    st.session_state.messages.append({"role": "assistant", "content": chatbot_message})

