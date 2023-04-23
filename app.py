import json
from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/student/<code>")
def quiz(code):
    return render_template("quiz.html", code=code)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/display/<code>")
def display(code):
    return render_template("displaycode.html", code=code)

@app.route("/addroom", methods=['POST'])
def addroom():
    data = json.loads(request.data)
    path = "static/rooms.json"
    with open(path) as f:
        roomdata = json.load(f)
    roomdata.update(data)
    with open(path, 'w') as f:
        json.dump(roomdata, f)
    return 'cool'

@app.route("/join")
def join():
    return render_template("join.html")

@app.route("/help/<question>/<selected>/<correct>")
def chat(question, selected, correct):
    key = os.environ["OPENAI_API_KEY"]
    return render_template("chat.html", key=key, question=question, selected=selected, correct=correct)

