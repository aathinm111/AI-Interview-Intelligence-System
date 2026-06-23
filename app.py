import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()


from langchain_groq import ChatGroq

from utils.pdf_reader import extract_text_from_pdf

from utils.retriever import (
    chunk_text,
    store_chunks,
    retrieve_chunks
)

from agents.hr_agent import hr_agent
from agents.tech_agent import tech_agent
from agents.ats_agent import ats_agent

st.set_page_config(
    page_title="AI Interview Intelligence System",
    layout="wide"
)

st.title("🤖 AI Interview Intelligence System")

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

uploaded_files = st.file_uploader(
    "Upload Resume / JD / PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    all_text = ""

    for file in uploaded_files:

        text = extract_text_from_pdf(file)

        all_text += text

    chunks = chunk_text(all_text)

    store_chunks(chunks)

    st.success("Documents Processed Successfully!")

agent_type = st.selectbox(

    "Choose AI Agent",

    [
        "HR Interview Agent",
        "Technical Interview Agent",
        "ATS Resume Analyzer"
    ]
)

user_question = st.text_input(
    "Ask Your Question"
)

if user_question:

    context_chunks = retrieve_chunks(
        user_question
    )

    context = "\n".join(
        context_chunks
    )

    if agent_type == "HR Interview Agent":

        system_prompt = hr_agent()

    elif agent_type == "Technical Interview Agent":


        system_prompt = tech_agent()

    else:

        system_prompt = ats_agent()

    final_prompt = f"""
    {system_prompt}

    Context:
    {context}

    Question:
    {user_question}

    Give detailed professional answer.
    """

    response = llm.invoke(
        final_prompt
    )

    st.subheader("AI Response")

    st.write(response.content)