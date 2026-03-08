# 🤖 HuggingFace LLM Chatbot

A simple **ChatGPT‑like AI chatbot** built using **Streamlit**,
**Hugging Face Inference API**, and **SQLite** for storing chat history.

This project demonstrates how to build a lightweight conversational AI
system that can generate responses using a large language model and
store previous conversations.

------------------------------------------------------------------------

# 🚀 Features

-   ChatGPT‑style question and answer chatbot
-   Uses Hugging Face hosted LLM (Qwen2.5‑72B‑Instruct)
-   Streamlit based web interface
-   SQLite database for chat history
-   Environment variable security using `.env`
-   Simple modular Python structure

------------------------------------------------------------------------

# 🧠 Model Used

Model:

Qwen/Qwen2.5-72B-Instruct

Accessed via Hugging Face Inference API.

------------------------------------------------------------------------

# 📂 Project Structure

    huggingface_llm_chatbot/
    │
    ├── app.py                # Streamlit UI
    ├── huggingface_llm.py   # LLM connection and response generation
    ├── database.py          # SQLite database for chat history
    ├── chat.db              # Database file (auto created)
    ├── .env                 # HuggingFace API token
    ├── .gitignore
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# ⚙️ Installation

## 1 Clone Repository

    git clone https://github.com/yourusername/huggingface_llm_chatbot.git

    cd huggingface_llm_chatbot

------------------------------------------------------------------------

# 📦 Install Dependencies

    pip install -r requirements.txt

------------------------------------------------------------------------

# 🔑 Environment Variables

Create a `.env` file in the project root:

    HUGGINGFACE_TOKEN=your_huggingface_api_token

Never upload this file to GitHub.

------------------------------------------------------------------------

# ▶️ Run the Application

Start the Streamlit server:

    streamlit run app.py

The chatbot will open in your browser.

------------------------------------------------------------------------

# 💬 How It Works

1.  User enters a question in the Streamlit interface
2.  `app.py` sends the prompt to `huggingface_llm.py`
3.  Hugging Face LLM generates a response
4.  Question and answer are saved in SQLite (`database.py`)
5.  Chat history appears in the sidebar

------------------------------------------------------------------------

# 🗄 Database

The chatbot stores conversations in:

    chat.db


------------------------------------------------------------------------

# 🛠 Technologies Used

-   Python
-   Streamlit
-   Hugging Face Inference API
-   SQLite
-   python-dotenv

------------------------------------------------------------------------

# 📌 Future Improvements

-   Add chat message UI like ChatGPT
-   Streaming responses
-   Multiple LLM model support
-   Vector database memory
-   User authentication

------------------------------------------------------------------------


