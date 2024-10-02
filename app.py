import streamlit as st
from modules.pdf_processing import get_pdf_text, get_text_chunks
from modules.embeddings import get_vector_store, user_input
from modules.chat_chain import clear_chat_history
from modules.feedback_analysis import (
    analyze_most_asked_topics,
    analyze_response_accuracy,
    list_incorrect_responses,
)

def main():
    st.set_page_config(page_title="ChatBot de Seguros", page_icon="🤖")
    st.title("ChatBot de Seguros ")
    st.write("Bem-vindo! Faça perguntas sobre os seguros.")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Faça upload de alguns PDFs e faça uma pergunta."}
        ]
        st.session_state.perguntas = []
        st.session_state.respostas = []
        st.session_state.avaliacoes = []
        st.session_state.chat_history = []

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Faça upload de PDFs", accept_multiple_files=True, type=['pdf'])
        if st.button("Processar"):
            if pdf_docs:
                with st.spinner("Processando..."):
                    raw_text = get_pdf_text(pdf_docs)
                    if not raw_text.strip():
                        st.warning("Os PDFs enviados não contêm texto extraível.")
                    else:
                        text_chunks = get_text_chunks(raw_text)
                        get_vector_store(text_chunks)
                        st.success("Processamento concluído!")
            else:
                st.warning("Por favor, faça upload de pelo menos um arquivo PDF.")

        if st.button('Limpar Histórico de Chat'):
            clear_chat_history()

        if st.checkbox('Analisar Temas Mais Questionados'):
            st.subheader("Temas Mais Questionados")
            most_common = analyze_most_asked_topics()
            if most_common:
                for word, count in most_common:
                    st.write(f"{word}: {count} vezes")
            else:
                st.write("Nenhuma interação registrada.")

        if st.checkbox('Analisar Assertividade das Respostas'):
            accuracy = analyze_response_accuracy()
            if accuracy is not None:
                st.subheader("Assertividade das Respostas")
                st.write(f"A assertividade das respostas é de {accuracy:.2f}%")
            else:
                st.write("Nenhum feedback disponível.")

        if st.checkbox('Listar Respostas Incorretas'):
            incorrect_responses = list_incorrect_responses()
            st.subheader("Respostas Incorretas")
            if incorrect_responses:
                for res in incorrect_responses:
                    st.write(f"Data/Hora: {res['timestamp']}")
                    st.write(f"Pergunta: {res['user_question']}")
                    st.write(f"Resposta: {res['assistant_response']}")
                    st.write("---")
            else:
                st.write("Nenhuma resposta incorreta registrada.")

    for i, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.write(message["content"])

            if message["role"] == "assistant" and "feedback" not in message:
                feedback = st.radio("A resposta foi útil?", ("Sim", "Não"), key=f"feedback_{i}")
                st.session_state.messages[i]["feedback"] = feedback

    if prompt := st.chat_input("Digite sua pergunta"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                response = user_input(prompt)
                st.write(response)

        if response:
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
