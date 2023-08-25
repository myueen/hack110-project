from flask import Flask, render_template, request

# a python library to fetch APIs -- different from request in the flask library
import requests

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('question_1.html')

@app.route('/question_1', methods=["GET", "POST"])
def question_1():
    if request.method == "POST":
        # TODO: add error if no answer was selected 
        return render_template("question_2.html")
    return render_template("question_1.html")


if __name__ == '__main__':
    app.run(debug=True)
