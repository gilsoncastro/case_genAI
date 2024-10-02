import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
import google.generativeai as genai
genai.configure(api_key=api_key)

# Função para gerar o índice FAISS a partir dos fragmentos de texto
def get_vector_store(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local("data/faiss_index")
    

# Função para obter a resposta baseada em embeddings e pergunta do usuário
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local("data/faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = vector_store.similarity_search(user_question)

    from modules.chat_chain import get_conversational_chain
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    return response['output_text']