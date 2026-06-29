# 📄 ResearchGPT — AI Research Paper Assistant

An intelligent NLP and LLM-based application that helps students, researchers, and professionals quickly understand and interact with research papers.

## 🚀 Features

- 📤 Upload PDF research papers
- 📝 Auto-generate concise summaries
- 🔑 Extract keywords automatically
- 🧠 Detect topics and named entities
- 💬 Ask questions in natural language (RAG-based Q&A)
- ⬇️ Download summary as TXT or PDF

## 🛠️ Technologies Used

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| LLM | Groq API (LLaMA 3.3) |
| Embeddings | HuggingFace (MiniLM) |
| Vector DB | FAISS |
| PDF Processing | PyPDF2 |
| NLP | spaCy, NLTK |
| Framework | LangChain |

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ResearchGPT.git
cd ResearchGPT
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Set up environment variables
Create a `.env` file:

GROQ_API_KEY=your_groq_api_key_here


## 🔑 Get Groq API Key

1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign up for free
3. Create an API key
4. Paste it in your `.env` file

## 📸 Demo

> Upload a research paper PDF → Get instant summary, keywords, topics, and chat with the paper!

## 👩‍💻 Author

**VAISHNAVI**  
[GitHub](https://github.com/Vaishnavi-developer-1) • [LinkedIn](https://www.linkedin.com/in/vaishnavi-r-135360259/)

### 5. Run the app
```bash
streamlit run app.py
```
