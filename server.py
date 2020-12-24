
from flask import Flask, render_template, flash, redirect, url_for
from flask import request
from flask import session

import sys
# from Test.test_ui import *
from config import Config

from Database.connection import *
from Database.entity import *
from Database.account import *

from Forms.account import *
from Forms.entity import *

from Objects.entity import *
from Objects.account import *

from Database.association import *

from test_ui import *

# --------pre calculation-----------
app = Flask(__name__)
app.config.from_object(Config)
conn, cur = connect_db()
print("Server start.")
# --------end of pre calculation-----------



@app.route("/")
@app.route('/listGlobalPosts')
def index():
	postDao = PostDao(conn, cur)
	public_posts = postDao.select_public()
	if "USERNAME" in session:
		useremail = session['USERNAME']
	else:
		useremail = None
	return render_template("list_global_posts.html", posts=public_posts, userEmail=useremail)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		new_user = RegisterForm_to_User(form)

		userDao = UserDao(conn, cur)

		if userDao.check_exist(new_user.get_username()):
			return "User already exists"
		else:
			userDao.to_db(new_user)
			session['USERNAME'] = new_user.get_username()
			session['USERID'] = new_user.get_id()
			return redirect(url_for('index'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():

		username = form.username.data
		password = form.password.data
		userDao = UserDao(conn, cur)
		check = userDao.check(username, password)

		if check:
			# url_for('function_name')
			session['USERNAME'] = username
			session['USERID'] = userDao.get_user_id(username)
			return redirect(url_for('index'))
		else:
			return redirect(url_for('login'))
	return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
	session['USERNAME'] = None
	session['USERID'] = None
	return render_template("list_global_posts.html", posts=posts)

@app.route("/listPersons")
def list_persons():
	personDao = PersonDao(conn, cur)
	records = personDao.list_by_user(session['USERID'])
	persons = personDao.entities_to_objects(records)
	return render_template("list_persons.html", persons=persons, userEmail=session['USERNAME'])

@app.route("/listGroups")
def list_groups():
	groupDao = GroupDao(conn, cur)
	records = groupDao.list_by_user(session['USERID'])
	groups = groupDao.entities_to_objects(records)
	return render_template("list_groups.html", groups=groups, userEmail=session['USERNAME'])


@app.route("/listPosts")
def list_posts():
	postDao = PostDao(conn, cur)
	records = postDao.list_by_user(session['USERID'])
	posts = postDao.entities_to_objects(records)
	return render_template("list_posts.html", posts=posts, userEmail=session['USERNAME'])

@app.route("/viewPerson")
def view_person():
	id = request.args.get('id')
	personDao = PersonDao(conn, cur)
	person = personDao.select_by_id(id)
	return render_template("view_person.html", person=person, groups=groups, posts=posts, userEmail=session['USERNAME'])

@app.route("/viewGroup")
def view_group():
	id = request.args.get('id')
	groupDao = GroupDao(conn, cur)
	group = groupDao.select_by_id(id)
	person_group_dao = PersonGroupDao(conn, cur)
	persons_in_group = person_group_dao.get_persons_in_group(id, session['USERID'])
	return render_template("view_group.html", group=group, personsInGroup=persons_in_group, postsOfGroup=posts, userEmail=session['USERNAME'])

@app.route("/viewPost")
def view_post():
	id = request.args.get('id')
	postDao = PostDao(conn, cur)
	post = postDao.select_by_id(id)
	return render_template("view_post.html", post=post, personsWithPost=None, groupsWithPost=None, userEmail=session['USERNAME'])

@app.route("/addPerson", methods=['GET', 'POST'])
def add_person():
	form = PersonForm()
	if form.validate_on_submit():
		new_person = PersonFrom_to_Person(form, session['USERID'])
		personDao = PersonDao(conn, cur)
		personDao.to_db(new_person)

		return redirect(url_for('list_persons'))
	return render_template('add_person.html', title='Add Person', form=form, userEmail=session['USERNAME'])


@app.route("/addGroup", methods=['GET', 'POST'])
def add_group():
	form = GroupForm()
	if form.validate_on_submit():
		new_group = GroupForm_to_Group(form, session['USERID'])
		groupDao = GroupDao(conn, cur)
		groupDao.to_db(new_group)

		return redirect(url_for('list_groups'))
	return render_template('add_group.html', title='Add Group', form=form, userEmail=session['USERNAME'])

@app.route("/addPost", methods=['GET', 'POST'])
def add_post():
	form = PostForm()
	if form.validate_on_submit():
		new_post = PostForm_to_Post(form, session['USERID'])
		postDao = PostDao(conn, cur)
		postDao.to_db(new_post)

		return redirect(url_for('list_posts'))
	return render_template('add_post.html', title='Add Post', form=form, userEmail=session['USERNAME'])

@app.route("/addSocialMedia", methods=['GET', 'POST'])
def add_social_media():
	person_id = request.args.get("personId")

	form = SocialMediaForm()
	if form.validate_on_submit():

		return redirect(url_for('view_person'))
	return render_template('add_social_media.html', title='Add Social Media', form=form, userEmail=session['USERNAME'])


@app.route("/deletePerson")
def delete_person():
	person_id = request.args.get("id")
	personDao = PersonDao(conn, cur)
	personDao.delete(person_id)
	return redirect(url_for("list_persons"))


@app.route("/deleteGroup")
def delete_group():
	group_id = request.args.get("id")
	groupDao = GroupDao(conn, cur)
	groupDao.delete(group_id)
	return redirect(url_for("list_groups"))

@app.route("/deletePost")
def delete_post():
	post_id = request.args.get("id")
	postDao = PostDao(conn, cur)
	postDao.delete(post_id)
	return redirect(url_for("list_posts"))

@app.route("/addPersonToGroup/list")
def list_persons_not_in_group():
	group_id = request.args.get("id")
	user_id = session['USERID']
	person_group_dao = PersonGroupDao(conn, cur)
	persons_not_in_group = person_group_dao.get_persons_not_in_group(group_id, user_id)

	return render_template("choose_person.html", persons=persons_not_in_group, group_id=group_id, userEmail=session['USERNAME'])

@app.route("/addPersonToGroup")
def add_person_to_group():
	person_id = request.args.get("id")
	group_id = request.args.get("groupId")
	person_group_dao = PersonGroupDao(conn, cur)
	person_group_dao.add_assoc(person_id, group_id, session['USERID'])

	return redirect(url_for('list_groups'))

@app.route("/tagPersonWithPost/list")
def list_persons_not_in_post():
	post_id = request.args.get("id")
	user_id = session['USERID']
	person_post_dao = PersonPostDao(conn, cur)
	persons_not_in_post = person_post_dao.get_persons_not_in_post(post_id, user_id)

	return render_template("choose_person.html", persons=persons_not_in_post, post_id=post_id, userEmail=session['USERNAME'])

@app.route("/tagPersonWithPost")
def add_person_to_post():
	person_id = request.args.get("id")
	post_id = request.args.get("postId")
	person_post_dao = PersonPostDao(conn, cur)
	person_post_dao.add_assoc(person_id, post_id, session['USERID'])

	return redirect(url_for('list_posts'))
