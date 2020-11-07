
from flask import Flask, render_template
import sys
from Test.test_ui import *


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():

    return render_template('index.html')

@app.route("/listPersons")
def list_persons():
	
	return render_template("list_persons.html", persons=persons)

@app.route("/viewPerson")
def view_person():
	
	return render_template("view_person.html", person=persons[0], groups=groups, posts=posts)

@app.route("/viewGroup")
def view_group():

	return render_template("view_group.html", group=groups[0], personsInGroup=persons, postsOfGroup=posts)

@app.route("/addPerson", methods=['GET', 'POST'])
def add_person():

	return render_template("add_person.html")

@app.route("/listGroups")
def list_groups():

	return render_template("list_groups.html", groups=groups)


@app.route("/listPosts")
def list_posts():

	return render_template("list_posts.html", posts=posts)


# --------pre calculation-----------
print("Server start.")
# --------end of pre calculation-----------

