from flask import Flask, render_template

tema = Flask(__name__)

@tema.route("/")
def acasa():
    return render_template("homeworkhome.html")

@tema.route("/api/v1/<word>")
def homework(word):
    return {"definition" : word.upper(),
            "word" : word}

tema.run(debug=True, port=5001)
