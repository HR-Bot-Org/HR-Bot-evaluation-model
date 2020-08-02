from flask import Flask, render_template, request
from model1 import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/eval", methods=["POST"])
def eval():
    model_answer = request.form.get("model_answer")
    answer = request.form.get("answer")
    evaluation=model(model_answer, answer)
    return render_template("eval.html", evaluation= evaluation)

if __name__ == "__main__":
    app.run(debug=True)