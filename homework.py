from flask import Flask, render_template
import pandas as pd

tema = Flask(__name__)

dictionary = "G:\\PyhonProjects\\TheWeatherApp\\pythonProject1\\homeworkdict\\dictionary.csv"
df = pd.read_csv(dictionary)

"""
Dictionaru se incarca aici fiindca e un practice bun sa nu incarci lucruri in functii daca lucrurile sunt
statice. Asta fiindca nu vrei sa se ruleze un proces de fiecare data cand se ruleaza o functie decat daca e necesar
(ex: te astepti ca fisieru sa fie modificat de la ultimu run). Daca nu e necesar, ar tb incarcat in afara
functiei ca sa ruleze o data.
"""

@tema.route("/")
def acasa():
    return render_template("homeworkhome.html")

@tema.route("/api/v1/<word>")
def homework(word):
    definition = df.loc[df['word'] == word][ 'definition'].squeeze()
    print(definition)
    return {"definition": definition,
            "word": word}

tema.run(debug=True, port=5005)
#[ 'definition']