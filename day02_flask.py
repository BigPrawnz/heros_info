from flask import Flask,render_template
from flask import url_for
app = Flask(__name__)
name = "League Of Legends"
heros = [
	{"title":"anni","name":"Annie"},
	{"title":"aolafu","name":"Olaf"},
	{"title":"jialiao","name":"Galio"},
	{"title":"kapai","name":"TwistedFate"},
	{"title":"zhaoxin","name":"XinZhao"},
	{"title":"ejiate","name":"Urgot"},
	{"title":"lefulan","name":"Leblanc"},
	{"title":"xixuegui","name":"Vladimir"}
]
@app.route("/")
def index():
	return render_template("index.html",name=name,heros=heros)
if __name__ == '__main__':
    app.run(debug=True)