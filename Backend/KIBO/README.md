# 🏛️ GovSchemesHub

An AI-powered platform to search, analyze, and understand government schemes using **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Features

- 🔍 Search government schemes easily
- 🤖 AI-powered answers using LLM
- 📄 Document-based retrieval system
- ⚡ Fast and relevant responses using vector database
- 🧠 Context-aware responses using RAG pipeline

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Vector Database (FAISS / Chroma)**
- **OpenAI / LLM APIs**
- **Document Loaders & Text Chunking**

---

## 📂 Project Structure

GovSchemesHub/
|── Backend/
    |│── python_main.py             # Main entry point
     │── document_loader.py         # Loads scheme      documents
     │── chunks.py                  # Text chunking logic
     │── vectorDB.py                # Vector database      setup
     │── retriever.py               # Retrieval logic
     │── llm_chain.py               # LLM pipeline (RAG)
     │── .env                       # Environment variables      (ignored)
     │── .gitignore                 # Ignored files
     │── README.md
     
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
git clone https://github.com/poonamlodwal/GovSchemesHub.git
cd GovSchemesHub

### 2️⃣ Create Virtual Environment

python -m venv venv
source venv/bin/activate # (Linux/Mac)
venv\Scripts\activate # (Windows)


### 3️⃣ Install Dependencies

pip install -r requirements.txt


### 4️⃣ Setup Environment Variables

Create a `.env` file:

OPENAI_API_KEY=your_api_key_here


⚠️ Never push `.env` to GitHub

---

## ▶️ Run the Project

python python_main.py


---

## 🧠 How It Works

1. Documents are loaded using `document_loader.py`
2. Text is split into chunks
3. Chunks are converted into embeddings
4. Stored in a vector database
5. User query is matched with relevant chunks
6. LLM generates a final answer using context

---

## 📌 Use Cases

- Government scheme discovery
- Student assistance tools
- Public service platforms
- AI-based search systems

---

## ⚠️ Security Note

- Do NOT expose API keys
- `.env` file is ignored using `.gitignore`
- If leaked, revoke keys immediately

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## 📜 License

This project is licensed under the MIT License.


🖥️ Streamlit UI (app.py)
---
import streamlit as st
from retriever import get_relevant_docs
from llm_chain import get_llm_response

# Page config
st.set_page_config(
    page_title="GovSchemesHub",
    page_icon="🏛️",
    layout="wide"
)

# Title
st.title("🏛️ GovSchemesHub")
st.markdown("### AI-powered Government Scheme Assistant")

# Sidebar
st.sidebar.header("⚙️ Settings")
user_name = st.sidebar.text_input("Enter your name", "User")
top_k = st.sidebar.slider("Number of results", 1, 10, 3)

st.sidebar.markdown("---")
st.sidebar.info("Built using RAG + LLM")

# Main input
query = st.text_input("🔍 Ask about any government scheme:")

# Button
if st.button("Search"):
    if query.strip() == "":
        st.warning("Please enter a query!")
    else:
        with st.spinner("🔎 Searching and generating answer..."):

            # Step 1: Retrieve docs
            docs = get_relevant_docs(query, k=top_k)

            # Step 2: Generate response
            response = get_llm_response(query, docs)

        # Output
        st.success("✅ Answer generated!")

        st.markdown("### 🤖 AI Response")
        st.write(response)

        # Expandable section
        with st.expander("📄 Retrieved Context"):
            for i, doc in enumerate(docs):
                st.markdown(f"**Document {i+1}:**")
                st.write(doc)

# Footer
st.markdown("---")
st.markdown(f"👋 Hello {user_name}, thanks for using GovSchemesHub!")

✅ retriever.py

def get_relevant_docs(query, k=3):
    # return list of relevant text chunks
    return docs

✅ llm_chain.py

def get_llm_response(query, docs):
    # return final answer string
    return response

📦 Install Streamlit

pip install streamlit

▶️ Run the App

streamlit run app.py
