from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
import streamlit as st

# Função para gerar a cadeia de conversa
def get_conversational_chain():
    prompt_template = """
    Você é um assistente de seguros, responda à pergunta o mais detalhadamente possível a partir do contexto fornecido.
    Se a resposta não estiver no contexto fornecido, diga "A resposta não está disponível no contexto".

    Contexto: {context}
    Questão: {question}
    Resposta:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)
    return chain

# Função para limpar o histórico de chat
def clear_chat_history():
    st.session_state.messages = [
        {"role": "assistant", "content": "Faça upload de alguns PDFs e faça uma pergunta."}]
    st.session_state.chat_history = []
    st.session_state.perguntas = []
    st.session_state.respostas = []
    st.session_state.avaliacoes = []
