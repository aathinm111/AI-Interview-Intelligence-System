# 🤖 AI Interview Intelligence System

An AI-powered interview preparation platform built using **Streamlit, LangChain, Groq LLM, and ChromaDB**. The system helps users prepare for interviews by providing HR interview guidance, technical interview assistance, and ATS-based resume analysis.

## 🚀 Features

### 👨‍💼 HR Interview Agent

* Generates HR interview questions and answers.
* Provides professional and behavioral interview guidance.
* Helps users improve communication and confidence.

### 💻 Technical Interview Agent

* Answers technical interview questions.
* Supports Data Science, Machine Learning, Python, SQL, and AI concepts.
* Generates detailed explanations and interview preparation content.

### 📄 ATS Resume Analyzer

* Analyzes resumes against job descriptions.
* Identifies missing skills and keywords.
* Provides suggestions to improve ATS compatibility.

### 📚 Document Processing

* Upload Resume, Job Description, or PDF documents.
* Extracts and processes document content.
* Uses semantic search for context-aware responses.

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Groq API
* ChromaDB
* PyMuPDF / PDF Processing
* Vector Embeddings

## 📂 Project Structure

```text
AI-Interview-Intelligence-System/
│
├── agents/
│   ├── ats_agent.py
│   ├── hr_agent.py
│   └── tech_agent.py
│
├── utils/
│   ├── embeddings.py
│   ├── pdf_reader.py
│   └── retriever.py
│
├── app.py
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/aathinm111/AI-Interview-Intelligence-System.git
cd AI-Interview-Intelligence-System
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

## 🎯 Use Cases

* Interview Preparation
* Resume Evaluation
* ATS Optimization
* Technical Skill Assessment
* Career Guidance

## 📸 Application Workflow

1. Upload Resume / Job Description PDF.
2. Select the required AI Agent.
3. Ask interview-related questions.
4. Receive AI-generated responses with document context.

## 👨‍💻 Author

**Aathi Narayanamoorthi**

* MSc Mathematics
* Data Science & AI Enthusiast
* Interested in Machine Learning, Generative AI, and LLM Applications

## ⭐ Future Enhancements

* Voice-based interview simulation
* Multi-language support
* Real-time interview scoring
* Interview performance analytics
* AI-powered career recommendations
