import streamlit as st
from huggingface_llm import generate_answer
from database import save_chat, load_chats

st.set_page_config(page_title="AI Chatbot")

st.title("AI Chatbot")

# Sidebar History
st.sidebar.title("Chat History")

history = load_chats()

for chat in history:
    st.sidebar.write("Q:", chat[1])

# Main Chat Area
question = st.text_input("Ask your question")

if st.button("Send"):

    answer = generate_answer(question)

    save_chat(question,answer)

    st.write("### Question")
    st.write(question)

    st.write("### Answer")
    st.write(answer)