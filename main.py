from atcoder_problems import atcoder_propagate
from models import question, problem_set
from flask import Flask, render_template, redirect, request, url_for
import json

#Server imports
from gevent.pywsgi import WSGIServer
import os

if os.name != "nt":
    os.chdir(os.path.dirname(_file_))

#problem_sets = list()
#atcoder_propagate(problem_sets=problem_sets, username="shoryu386")

"""
with open("problemsets.txt", "w", encoding="utf-8") as file:
    for problem_set_item in problem_sets:
        file.writelines(problem_set_item.returnStringList())
"""

app = Flask(__name__, template_folder="templates")

atcoder_categories = None

with open("atcoder_tags.json") as file:
    atcoder_categories = json.load(file)

@app.route("/", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.form.get('username')
        return redirect(url_for('index', username=username))

@app.route("/<username>", methods=['POST', 'GET'])
def index(username):
    problem_sets = list()
    atcoder_propagate(problem_sets=problem_sets, username=username)
    return render_template("index.html", problem_sets=problem_sets, atcoder_categories=atcoder_categories)

if __name__ == "__main__":
    #http_server = WSGIServer(("0.0.0.0", 2001), app)
    #http_server.serve_forever()
    app.run(host="0.0.0.0", debug=True)