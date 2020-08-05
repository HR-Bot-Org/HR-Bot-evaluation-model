from flask import Flask, request, abort, jsonify
from evaluator import Evaulator
from feedback import FeedBack

evaluator = Evaulator()
app = Flask(__name__)

@app.route('/')
def index():
    return "Machine Learning Models For HR-Bot"

@app.route('/evaluate')
def evaluation():
    if not request.json or not 'answers' in request.json or not 'applicant_answer' in request.json:
        abort(400)

    model_answers = list(request.json['answers'])
    applicant_answer = str(request.json['applicant_answer'])
    answers = model_answers
    answers.append(applicant_answer)
    score = evaluator.evalute_applicant_answer(answers)
    return jsonify({'score': str(score)}), 200


@app.route('/feedback')
def feedback():
    if not request.json or not 'skill' in request.json or not 'question' in request.json:
        abort(400)

    skill = str(request.json['skill'])
    question = str(request.json['question'])

    f = FeedBack(skill, question)
    my_feedback = f.search()
    return jsonify({'feedback': str(my_feedback)}), 200


if __name__ == "__main__":
    app.run(debug=True)