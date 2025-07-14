import streamlit as st
from typing import List, Dict
from chatbot_init import client as chatbot, MODEL
from rich import print
from topic_categorization import classify_question
from vector_store import embed
import chromadb


st.set_page_config(page_title="Chatbot", page_icon="🤖")

st.title("🤖 Streamlit Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You're a RAG powered chatbot. \nYou might get two user messages at the same time. Do not say that this is user's context. Provide answer as if you knew about it."}]

# Display chat history
for chat in st.session_state.chat_history[1:]:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send message to OpenAI and get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            topic = classify_question(user_input)
            vdb_client = chromadb.PersistentClient(path="./vector-db")
            collection = vdb_client.get_or_create_collection(name=topic)

            embedded_question = embed(user_input)
            most_relevant_documents = collection.query(
                query_embeddings=[embedded_question], n_results=5)
            most_relevant_texts = most_relevant_documents["documents"][0]

            context = [{"role": "user",
                        "content": f"context for answering the previous question/questions: {";".join(most_relevant_texts)}"}]
            print(context)
            response = chatbot.chat.completions.create(
                model=MODEL,
                messages=st.session_state.chat_history + context,
            )
            assistant_reply = response.choices[0].message.content
            st.markdown(assistant_reply)

        # Add assistant response to chat history
        st.session_state.chat_history.append(
            {"role": "assistant", "content": assistant_reply})
