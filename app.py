from flask import Flask, request, abort, jsonify
# from evaluator import Evaulator
from feedback import FeedBack

# evaluator = Evaulator()
app = Flask(__name__)

@app.route('/')
def index():
    return "Machine Learning Models For HR-Bot"

# @app.route('/evaluate')
# def evaluation():
#     if not request.json or not 'answers' in request.json or not 'applicant_answer' in request.json:
#         abort(400)

#     model_answers = list(request.json['answers'])
#     applicant_answer = str(request.json['applicant_answer'])
#     answers = model_answers
#     answers.append(applicant_answer)
#     score = evaluator.evalute_applicant_answer(answers)
#     return jsonify({'score': str(score)}), 200


# intput example : 
# {
#     "data" :
#     {
#         "question": "what is the desicion tree", 
#         "skills": 
#         [
#             {
#                 "name": "machine learning",
#                 "site": "www.datacamp.com"
#             },
#             {
#                 "name": "object oriented",
#                 "site":"www.datacamp.com"
#             }
#         ],
#         "token": "hr_bot_2019_2020"
#     }
# }
@app.route('/interview/feedback')
def feedback():
    if not request.json or not 'data' in request.json:
        abort(400)

    data = (request.json['data'])
    f = FeedBack(data=data)
    my_feedback = f.search()

    if my_feedback is None:
        abort(404)
        return "This should not be returned"
    else:
        return jsonify({'feedback': my_feedback}), 200


if __name__ == "__main__":
    app.run(debug=True)