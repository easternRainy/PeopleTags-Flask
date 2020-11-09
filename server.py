
from flask import Flask, render_template, flash, redirect, url_for
from flask import request

import sys
from Test.test_ui import *
from config import Config

from Database.connection import *
from Database.entity import *
from Database.account import *

from Forms.account import *
from Forms.entity import *

from Objects.entity import *
from Objects.account import *

# --------pre calculation-----------
app = Flask(__name__)
app.config.from_object(Config)
conn, cur = connect_db()
print("Server start.")
# --------end of pre calculation-----------



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
		new_user = RegisterForm_to_User(form)

		userDao = UserDao()
		userDao.to_db(new_user, conn, cur)

		return redirect(url_for('index_with_email', userEmail=new_user.username))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():

		username = form.username.data
		password = form.password.data
		userDao = UserDao()
		check = userDao.check(username, password, cur)

		if check:
			# url_for('function_name')
			return redirect(url_for('index_with_email', userEmail=username))
		else:
			return "Log in Failed"
	return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
	return render_template("list_global_posts.html", posts=posts)

@app.route("/listPersons")
def list_persons():
	personDao = PersonDao()
	records = personDao.list_by_user(cur)
	persons = personDao.entities_to_objects(records)
	return render_template("list_persons.html", persons=persons)

@app.route("/listGroups")
def list_groups():
	groupDao = GroupDao()
	records = groupDao.list_by_user(cur)
	groups = groupDao.entities_to_objects(records)
	return render_template("list_groups.html", groups=groups)


@app.route("/listPosts")
def list_posts():
	postDao = PostDao()
	records = postDao.list_by_user(cur)
	posts = postDao.entities_to_objects(records)
	return render_template("list_posts.html", posts=posts)

@app.route("/viewPerson")
def view_person():
	id = request.args.get('id')
	personDao = PersonDao()
	person = personDao.select_by_id(cur, id)
	return render_template("view_person.html", person=person, groups=groups, posts=posts, socialMedias=socialMedias)

@app.route("/viewGroup")
def view_group():
	id = request.args.get('id')
	groupDao = GroupDao()
	group = groupDao.select_by_id(cur, id)
	return render_template("view_group.html", group=group, personsInGroup=persons, postsOfGroup=posts)

@app.route("/viewPost")
def view_post():

	return render_template("view_post.html", post=posts[0], personsWithPost=persons, groupsWithPost=groups)

@app.route("/addPerson", methods=['GET', 'POST'])
def add_person():
	form = PersonForm()
	if form.validate_on_submit():
		new_person = PersonFrom_to_Person(form)
		personDao = PersonDao()
		personDao.to_db(new_person, conn, cur)

		return redirect(url_for('list_persons'))
	return render_template('add_person.html', title='Add Person', form=form)


@app.route("/addGroup", methods=['GET', 'POST'])
def add_group():
	form = GroupForm()
	if form.validate_on_submit():
		new_group = GroupForm_to_Group(form)
		groupDao = GroupDao()
		groupDao.to_db(new_group, conn, cur)

		return redirect(url_for('list_groups'))
	return render_template('add_group.html', title='Add Group', form=form)

@app.route("/addPost", methods=['GET', 'POST'])
def add_post():
	form = PostForm()
	if form.validate_on_submit():
		new_post = PostForm_to_Post(form)
		postDao = PostDao()
		postDao.to_db(new_post, conn, cur)

		return redirect(url_for('list_posts'))
	return render_template('add_post.html', title='Add Post', form=form)

@app.route("/addSocialMedia", methods=['GET', 'POST'])
def add_social_media():
	person_id = request.args.get("personId")

	form = SocialMediaForm()
	if form.validate_on_submit():

		return redirect(url_for('view_person'))
	return render_template('add_social_media.html', title='Add Social Media', form=form)



