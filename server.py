
from flask import Flask, render_template

import sys

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():

    return render_template('index.html', userEmail="secregister01@gmail.com")

@app.route("/listPersons")
def list_persons():

	return render_template("list_persons.html")

# --------pre calculation-----------
print("Server start.")
# --------end of pre calculation-----------

