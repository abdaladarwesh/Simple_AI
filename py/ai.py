import json
from difflib import get_close_matches

def loadDataFile(filePath) -> dict:
    with open(filePath, 'r') as file:
        data = json.load(file)
    return data

def updateDataFile(filePath, data: dict):
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

def main():
    data = loadDataFile('data.json')
    while True:
        question = input('You: ')
        if question == 'exit':
            break
        bestMatch: str = find_best_match(question, [q['question'] for q in data['questions']])
        if bestMatch:
            answer = get_answer(bestMatch, data)
            print(f'Bot: {answer}')
        else:
            print('Bot: Sorry, I do not know the answer. Can you teach me?')
            newAnswer = input('You: ')
            data['questions'].append({'question': question, 'answer': newAnswer})
            updateDataFile('data.json', data)
            print('Bot: Thank you for teaching me')

if __name__ == "__main__":
    main()
