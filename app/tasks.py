import os
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain 
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_community.document_loaders import PyPDFLoader

from dotenv import load_dotenv
load_dotenv()
# Ensure the OpenAI API key is set in the environment
llm = ChatOpenAI(model_name="gpt-4o-mini-2024-07-18", temperature=0.7)

def summarize_text(text):
    prompt = PromptTemplate.from_template("Summarize the following text:\n{text}")
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"text":text})
def change_tone(text, tone):
    prompt = PromptTemplate.from_template(f"Rewrite the following text in a {tone} tone:\n{text}")
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"text":text, "tone": tone})
def ask_question_about_doc(question):
    db = FAISS.load_local("data/embeddings", OpenAIEmbeddings())
    docs = db.similarity_search(question)
    qa_chain = load_qa_chain(llm=llm, chain_type="stuff")
    return qa_chain.run(input_documents=docs, question=question)
def explain_code(code):
    prompt = PromptTemplate.from_template("Explain the following code:\n{code}")
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"code": code})