
from flask import Flask, render_template

import sys

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():

    return render_template('index.html')

@app.route("/listPersons")
def list_persons():
	persons = []
	sicheng = {"first":"Sicheng", "last": "Zhou", "jobTitle": "Full Stack Developer", "description":"Crazy Guy"}
	persons.append(sicheng)
	return render_template("list_persons.html", persons=persons)

@app.route("/viewPerson")
def view_person():
	sicheng = {"first":"Sicheng", "last": "Zhou", "jobTitle": "Full Stack Developer", "description":"Crazy Guy"}
	socialMedias = [{}]
	groups = [{}]
	return render_template("view_person.html", person=sicheng, socialMedias=socialMedias, groups=groups)

# --------pre calculation-----------
print("Server start.")
# --------end of pre calculation-----------

