import json
from difflib import get_close_matches

def loadDataFile(filePath) -> dict:
    with open(filePath, 'r') as file:
        data = json.load(file)
    return data

def updateDataFile(filePath, new_entry: dict):
    try:
        with open(filePath, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'questions': []}

    data['questions'].append(new_entry)

    with open(filePath, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question, questions: list) -> str:
    best_match: list = get_close_matches(user_question, questions, n=1, cutoff=0.8)
    return best_match[0] if best_match else None

def get_answer(question, data: dict) -> str:
    for q in data['questions']:
        if q['question'].lower() == question.lower():
            return q['answer']
    return None

