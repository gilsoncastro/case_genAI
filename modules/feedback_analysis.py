from modules.utils import (
    log_feedback,
    analyze_most_asked_topics,
    analyze_response_accuracy,
    list_incorrect_responses
)

# Definir os caminhos dos arquivos de log
CHAT_LOG_FILE = "data/chat_log.csv"
FEEDBACK_LOG_FILE = "data/feedback_log.csv"

# Função para registrar o feedback da interação
def log_user_feedback(user_question, assistant_response, feedback):
    log_feedback(FEEDBACK_LOG_FILE, user_question, assistant_response, feedback)

# Função para analisar os temas mais frequentes
def analyze_frequent_topics():
    return analyze_most_asked_topics(CHAT_LOG_FILE)

# Função para analisar a assertividade das respostas
def analyze_accuracy():
    return analyze_response_accuracy(FEEDBACK_LOG_FILE)

# Função para listar respostas incorretas
def list_incorrect_answers():
    return list_incorrect_responses(FEEDBACK_LOG_FILE)

