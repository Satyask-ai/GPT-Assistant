import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tasks import summarize_text, change_tone, ask_question_about_doc, explain_code
from utils.ingest import ingest_documents

st.set_page_config(page_title="Personal GPT Assistant", layout="wide")

st.title("Personal GPT Assistant")
st.subheader("Select a tesk below")

task = st.selectbox( "choose a task", [
    "summarize text",
    "Rewrite in Differernt Tone",
    "Ask a question about a document",  
    "Explain code in a document",
])
if task == "summarize text":
    user_input= st.text_area("Paste the text to summarize")
    if st.button("Summarize"):
        result = summarize_text(user_input)
        st.success(result)
elif task == "Rewrite in Differernt Tone":
     text = st.text_area("Paste the text")
     tone = st.selectbox("Select the tone", ["Formal", "Informal", "Friendly", "Professional"])
     if st.button("Rewrite"):
         rewritten_text = change_tone(text, tone)
         st.success(rewritten_text)
elif task == "Ask Questions from PDF":
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    if uploaded_file:
        ingest_documents(uploaded_file)
        question = st.text_input("Ask a question")
        if st.button("Answer"):
            answer = ask_question_about_doc( question)
            st.success(answer)
elif task == "Explain code":
    code_snippet = st.text_area("Paste the code")
    if st.button("Explain"):
        explanation = explain_code(code_snippet)
        st.success(explanation)