
from flask import Flask, render_template, flash, redirect, url_for
from flask import request

import sys
from Test.test_ui import *
from config import Config

from Forms.account import LoginForm, RegisterForm
from Forms.entity import PersonForm, GroupForm, PostForm, SocialMediaForm

app = Flask(__name__)
app.config.from_object(Config)
print(app.config['SECRET_KEY'])

@app.route("/")
@app.route('/listGlobalPosts')
def index():
    return render_template("list_global_posts.html", posts=posts)

@app.route('/listGlobalPosts/<userEmail>')
def index_with_email(userEmail):
	return render_template("list_global_posts.html", posts=posts, userEmail=userEmail)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		user = form.username.data
		return redirect(url_for('index_with_email', userEmail=user))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		# flash(f"Login requested for user {form.username.data} successed!")
		user = form.username.data

		# url_for('function_name')
		return redirect(url_for('index_with_email', userEmail=user))
	return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
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
	form = PersonForm()
	if form.validate_on_submit():

		return redirect(url_for('list_persons'))
	return render_template('add_person.html', title='Add Person', form=form)


@app.route("/addGroup", methods=['GET', 'POST'])
def add_group():
	form = GroupForm()
	if form.validate_on_submit():

		return redirect(url_for('list_groups'))
	return render_template('add_group.html', title='Add Group', form=form)

@app.route("/addPost", methods=['GET', 'POST'])
def add_post():
	form = PostForm()
	if form.validate_on_submit():

		return redirect(url_for('list_posts'))
	return render_template('add_post.html', title='Add Post', form=form)

@app.route("/addSocialMedia?personId=<person_id>", methods=['GET', 'POST'])
def add_social_media():
	person_id = request.args.get("personId")
	print(person_id)
	form = PersonForm()
	if form.validate_on_submit():

		return redirect(url_for('list_persons'))
	return render_template('add_social_media.html', title='Add Social Media', form=form)


# --------pre calculation-----------
print("Server start.")
# --------end of pre calculation-----------

