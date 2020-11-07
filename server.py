
from flask import Flask, render_template
import sys
from Test.test_ui import *


app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/listGlobalPosts")
def index():

    return render_template("list_global_posts.html", posts=posts)

@app.route("/listPersons")
def list_persons():
	
	return render_template("list_persons.html", persons=persons)

@app.route("/listGroups")
def list_groups():

	return render_template("list_groups.html", groups=groups)


@app.route("/listPosts")
def list_posts():

	return render_template("list_posts.html", posts=posts)

@app.route("/viewPerson")
def view_person():
	
	return render_template("view_person.html", person=persons[0], groups=groups, posts=posts, socialMedias=socialMedias)

@app.route("/viewGroup")
def view_group():

	return render_template("view_group.html", group=groups[0], personsInGroup=persons, postsOfGroup=posts)

@app.route("/viewPost")
def view_post():

	return render_template("view_post.html", post=posts[0], personsWithPost=persons, groupsWithPost=groups)

@app.route("/addPerson", methods=['GET', 'POST'])
def add_person():

	return render_template("add_person.html", person=persons[0])

@app.route("/addGroup", methods=['GET', 'POST'])
def add_group():

	return render_template("add_group.html", group=groups[0])

@app.route("/addPost", methods=['GET', 'POST'])
def add_post():

	return render_template("add_post.html", post=posts[0])


@app.route("/addSocialMedia", methods=['GET', 'POST'])
def add_social_media():

	return render_template("add_social_media.html", socialMedia=socialMedias[0])


# --------pre calculation-----------
print("Server start.")
# --------end of pre calculation-----------

