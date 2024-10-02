
# ChatBot de Seguros 

Este projeto é um **ChatBot interativo** que utiliza **PDFs** carregados pelo usuário para responder a perguntas sobre seguros. Ele é baseado em **IA generativa** e **Processamento de Linguagem Natural** (PLN) usando ferramentas como **Google Generative AI**, **LangChain** e **FAISS** para busca semântica.

## Estrutura do Projeto

chatbot/
│
├── app.py                    # Arquivo principal para execução do Streamlit
├── requirements.txt           # Dependências do projeto
├── .env                       # Variáveis de ambiente (API key)
├── data/                      # Diretório para PDFs, logs e índices FAISS
│   ├── faiss_index/           # Índice FAISS gerado pelos embeddings dos PDFs
│   ├── chat_log.csv           # Log de interações (perguntas e respostas)
│   └── feedback_log.csv       # Log de feedback dado pelos usuários
├── modules/                   # Pasta para módulos específicos
│   ├── pdf_processing.py      # Funções para processamento de PDF
│   ├── embeddings.py          # Funções para geração e gerenciamento de embeddings
│   ├── chat_chain.py          # Funções para gerar o chain de perguntas e respostas
│   ├── feedback_analysis.py   # Funções para análise de feedback e assertividade
│   └── utils.py               # Funções auxiliares (utilitárias)
└── README.md                  # Instruções do projeto

 streamlit run app.py

## Funcionalidades

- **Processamento de PDFs**: O usuário pode fazer upload de múltiplos PDFs que serão processados para extração de texto.
- **Divisão do texto em fragmentos**: O conteúdo dos PDFs é dividido em pedaços menores para melhor tratamento e busca.
- **Resposta a perguntas**: O chatbot responde a perguntas feitas com base no conteúdo dos PDFs processados.
- **Análise de feedback**: O projeto registra o feedback dos usuários para avaliar a assertividade das respostas.
- **Registro de interações**: Todas as perguntas e respostas são registradas em logs para análise posterior.
- **Busca Semântica**: Implementação do FAISS para fazer busca semântica nos textos extraídos dos PDFs.

## Instalação e Configuração

### 1. Requisitos

- Python 3.8 ou superior
- Virtualenv

### 2. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio/chatbot










