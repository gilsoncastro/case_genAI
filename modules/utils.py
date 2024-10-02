import os
import csv
from collections import Counter
import nltk
from nltk.corpus import stopwords
from datetime import datetime

# Função para escrever logs de interações em CSV
def log_interaction(file_path, user_question, assistant_response):
    fieldnames = ['timestamp', 'user_question', 'assistant_response']
    timestamp = datetime.now().isoformat()

    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'timestamp': timestamp,
            'user_question': user_question,
            'assistant_response': assistant_response
        })

# Função para registrar feedback em CSV
def log_feedback(file_path, user_question, assistant_response, feedback):
    fieldnames = ['timestamp', 'user_question', 'assistant_response', 'feedback']
    timestamp = datetime.now().isoformat()

    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'timestamp': timestamp,
            'user_question': user_question,
            'assistant_response': assistant_response,
            'feedback': feedback
        })

# Função para analisar os temas mais questionados
def analyze_most_asked_topics(file_path):
    questions = []

    if not os.path.isfile(file_path):
        return []

    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            questions.append(row['user_question'])

    stop_words = set(stopwords.words('portuguese'))
    words = []
    for question in questions:
        tokens = nltk.word_tokenize(question.lower())
        filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
        words.extend(filtered_tokens)

    word_counts = Counter(words)
    most_common = word_counts.most_common(10)
    return most_common

# Função para analisar a assertividade das respostas com base no feedback
def analyze_response_accuracy(file_path):
    total_feedback = 0
    positive_feedback = 0

    if not os.path.isfile(file_path):
        return None

    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_feedback += 1
            if row['feedback'] == 'Sim':
                positive_feedback += 1

    if total_feedback == 0:
        return None

    accuracy = (positive_feedback / total_feedback) * 100
    return accuracy

# Função para listar as respostas incorretas
def list_incorrect_responses(file_path):
    incorrect_responses = []

    if not os.path.isfile(file_path):
        return incorrect_responses

    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['feedback'] == 'Não':
                incorrect_responses.append({
                    'timestamp': row['timestamp'],
                    'user_question': row['user_question'],
                    'assistant_response': row['assistant_response']
                })

    return incorrect_responses
