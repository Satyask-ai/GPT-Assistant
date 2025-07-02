import os
from pypdf import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def ingest_documents(file):
    pdf = PdfReader(file)           
    text = ""       
    for page in pdf.pages:
        text += page.extract_text() 


    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs =  FAISS.from_documents(docs, embeddings)
    db.save_local("data/embeddings")