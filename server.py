
from flask import Flask, render_template, flash, redirect, url_for
from flask import request

import sys
from Test.test_ui import *
from config import Config

from Forms.login_form import LoginForm


app = Flask(__name__)
app.config.from_object(Config)
print(app.config['SECRET_KEY'])

@app.route("/")
def index():
    return render_template("list_global_posts.html", posts=posts)

@app.route('/listGlobalPosts/<userEmail>')
def index_with_email(userEmail):
	print("index with email is running")
	return render_template("list_global_posts.html", posts=posts, userEmail=userEmail)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		# flash(f"Login requested for user {form.username.data} successed!")
		user = form.username.data

		# url_for('function_name')
		return redirect(url_for('index_with_email', userEmail=user))
	return render_template('login.html', title='Sign In', form=form)

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
	if request.method == 'GET':
		return render_template("add_person.html", person={})
	else:
		# return render_template("add_person.html", person=persons[0])
		return "hello world"

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

