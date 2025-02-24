from flask import Flask, request, jsonify
from flask_restful import reqparse, Resource, Api, abort, fields
from ai import loadDataFile, updateDataFile, find_best_match, get_answer

app = Flask(__name__)
api = Api(app)

questions = reqparse.RequestParser()
questions.add_argument('question', type=str, required=True, help="you must enter a question")
questions.add_argument('answer', type=str, required=True, help="you must enter an answer")

class AI(Resource):
    
    def get(self):
        data = loadDataFile('data.json')
        return jsonify(data)
    
    def post(self):
        data = questions.parse_args()
        updateDataFile('data.json', data)
        return {"message": "Data updated successfully"}, 200
    
    def put(self):
        data = loadDataFile('data.json')
        question = request.get_json()
        best_match = find_best_match(question['question'], [q['question'] for q in data['questions']])
        if best_match:
            answer = get_answer(best_match, data)
            return {'question': question['question'], "answer": answer}, 200
        else:
            return {"message": "Answer cannot be found. Use the POST request to add it."}, 400

api.add_resource(AI, '/ai')

if __name__ == "__main__":
    app.run(debug=True)
