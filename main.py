from atcoder_problems import atcoder_propagate
from models import question, problem_set
from flask import Flask, render_template, redirect, request, url_for
#problem_sets = list()
#atcoder_propagate(problem_sets=problem_sets, username="shoryu386")

"""
with open("problemsets.txt", "w", encoding="utf-8") as file:
    for problem_set_item in problem_sets:
        file.writelines(problem_set_item.returnStringList())
"""

app = Flask(__name__, template_folder="templates")

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
    return render_template("index.html", problem_sets=problem_sets)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)