
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

# from test_ui import *

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
	return redirect(url_for("index"))

@app.route("/listPersons")
def list_persons():
	personDao = PersonDao(conn, cur)
	if "USERID" in session:
		user_id = session['USERID']
		username = session['USERNAME']
		records = personDao.list_by_user(user_id)
		persons = personDao.entities_to_objects(records)
	else:
		persons = None
		username = None

	return render_template("list_persons.html", persons=persons, userEmail=username)

@app.route("/listGroups")
def list_groups():
	groupDao = GroupDao(conn, cur)
	if "USERID" in session:
		user_id = session['USERID']
		username = session['USERNAME']
		records = groupDao.list_by_user(user_id)
		groups = groupDao.entities_to_objects(records)
	else:
		groups = None
		username = None

	return render_template("list_groups.html", groups=groups, userEmail=username)


@app.route("/listPosts")
def list_posts():
	postDao = PostDao(conn, cur)

	if "USERID" in session:
		user_id = session['USERID']
		username = session['USERNAME']
		records = postDao.list_by_user(user_id)
		posts = postDao.entities_to_objects(records)
	else:
		posts = None
		username = None

	return render_template("list_posts.html", posts=posts, userEmail=username)

@app.route("/viewPerson")
def view_person():
	id = request.args.get('id')
	personDao = PersonDao(conn, cur)
	person = personDao.select_by_id(id)
	person_group_dao = PersonGroupDao(conn, cur)
	user_id = session['USERID']
	groups = person_group_dao.get_groups_by_person(id, user_id)

	person_post_dao = PersonPostDao(conn, cur)
	posts = person_post_dao.get_posts_by_person(id, user_id)

	person_social_media_dao = PersonSocialMediaDao(conn, cur)
	social_medias = person_social_media_dao.get_social_medias_by_person(id, user_id)
	return render_template("view_person.html", person=person, groups=groups, posts=posts, socialMedias=social_medias, userEmail=session['USERNAME'])

@app.route("/viewGroup")
def view_group():
	id = request.args.get('id')
	groupDao = GroupDao(conn, cur)
	group = groupDao.select_by_id(id)
	person_group_dao = PersonGroupDao(conn, cur)

	user_id = session['USERID']
	persons_in_group = person_group_dao.get_persons_in_group(id, user_id)

	group_post_dao = GroupPostDao(conn, cur)
	posts_of_group = group_post_dao.get_posts_by_group(id, user_id)
	return render_template("view_group.html", group=group, personsInGroup=persons_in_group, postsOfGroup=posts_of_group, userEmail=session['USERNAME'])

@app.route("/viewPost")
def view_post():
	id = request.args.get('id')
	postDao = PostDao(conn, cur)
	post = postDao.select_by_id(id)

	user_id = session['USERID']
	persons = PersonPostDao(conn, cur).get_persons_in_post(id, user_id)
	groups = GroupPostDao(conn, cur).get_groups_in_post(id, user_id)
	return render_template("view_post.html", post=post, personsWithPost=persons, groupsWithPost=groups, userEmail=session['USERNAME'])

@app.route("/addPerson", methods=['GET', 'POST'])
def add_person():

	if "USERID" not in session or session["USERID"] is None:
		return "Please Log In"

	form = PersonForm()
	if form.validate_on_submit():
		new_person = PersonFrom_to_Person(form, session['USERID'])
		personDao = PersonDao(conn, cur)
		personDao.to_db(new_person)

		return redirect(url_for('list_persons'))
	return render_template('add_person.html', title='Add Person', form=form, userEmail=session['USERNAME'])



@app.route("/updatePerson", methods=['GET', 'POST'])
def update_person():

	id = request.args.get("id")
	person_dao = PersonDao(conn, cur)

	if request.method == 'GET':
		old_person = person_dao.select_by_id(id)
		form = old_person.to_form()
		return render_template('add_person.html', title='Add Person', form=form, userEmail=session['USERNAME'])
	else:
		form = PersonForm()
		user_id = session['USERID']
		if form.validate_on_submit():
			new_person = PersonFrom_to_Person(form, user_id, id=id
											  )
			person_dao.update(id, new_person)
			return redirect(url_for("view_person", id=id))
		return "Update Person Failed"


@app.route("/addGroup", methods=['GET', 'POST'])
def add_group():

	if "USERID" not in session or session["USERID"] is None:
		return "Please Log In"

	form = GroupForm()
	if form.validate_on_submit():
		new_group = GroupForm_to_Group(form, session['USERID'])
		groupDao = GroupDao(conn, cur)
		groupDao.to_db(new_group)

		return redirect(url_for('list_groups'))
	return render_template('add_group.html', title='Add Group', form=form, userEmail=session['USERNAME'])


@app.route("/updateGroup", methods=['GET', 'POST'])
def update_group():

	id = request.args.get("id")
	group_dao = GroupDao(conn, cur)

	if request.method == 'GET':
		old_group = group_dao.select_by_id(id)
		form = old_group.to_form()
		return render_template('add_group.html', title='Add Group', form=form, userEmail=session['USERNAME'])
	else:
		form = GroupForm()
		user_id = session['USERID']
		if form.validate_on_submit():
			new_group = GroupForm_to_Group(form, user_id, id=id)
			group_dao.update(id, new_group)
			return redirect(url_for("view_group", id=id))
		return "Update Group Failed"


@app.route("/addPost", methods=['GET', 'POST'])
def add_post():
	if "USERID" not in session or session["USERID"] is None:
		return "Please Log In"

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
		user_id = session['USERID']
		new_social_media = SocialMediaForm_to_SocialMedia(form, user_id)
		social_media_dao = SocialMediaDao(conn, cur)
		social_media_dao.to_db(new_social_media)

		person_social_media_dao = PersonSocialMediaDao(conn, cur)
		person_social_media_dao.add_assoc(person_id, new_social_media.get_id(), user_id)

		return redirect(url_for('view_person', id=person_id))
	return render_template('add_social_media.html', title='Add Social Media', form=form, userEmail=session['USERNAME'])


@app.route("/deleteSocialMedia")
def delete_social_media():
	person_id = request.args.get("personId")
	social_media_id = request.args.get("socialMediaId")
	user_id = session['USERID']
	social_media_dao = SocialMediaDao(conn, cur)
	social_media_dao.delete(social_media_id)
	person_social_media_dao = PersonSocialMediaDao(conn, cur)
	person_social_media_dao.delete_assoc(person_id, social_media_id, user_id)
	return redirect(url_for("view_person", id=person_id))

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

	return render_template("choose_person_to_group.html", persons=persons_not_in_group, group_id=group_id, userEmail=session['USERNAME'])

@app.route("/addPersonToGroup")
def add_person_to_group():
	person_id = request.args.get("id")
	group_id = request.args.get("groupId")
	person_group_dao = PersonGroupDao(conn, cur)
	person_group_dao.add_assoc(person_id, group_id, session['USERID'])

	return redirect(url_for('view_group', id=group_id))

@app.route("/tagPersonWithPost/list")
def list_persons_not_in_post():
	post_id = request.args.get("id")
	user_id = session['USERID']
	person_post_dao = PersonPostDao(conn, cur)
	persons_not_in_post = person_post_dao.get_persons_not_in_post(post_id, user_id)

	return render_template("choose_person_to_post.html", persons=persons_not_in_post, post_id=post_id, userEmail=session['USERNAME'])

@app.route("/tagPersonWithPost")
def add_person_to_post():
	person_id = request.args.get("id")
	post_id = request.args.get("postId")
	person_post_dao = PersonPostDao(conn, cur)
	person_post_dao.add_assoc(person_id, post_id, session['USERID'])

	return redirect(url_for('view_post', id=post_id))


@app.route("/tagGroupWithPost/list")
def list_groups_not_in_post():
	post_id = request.args.get("id")
	user_id = session['USERID']
	group_post_dao = GroupPostDao(conn, cur)
	groups_not_in_post = group_post_dao.get_groups_not_in_post(post_id, user_id)

	return render_template("choose_group_to_post.html", groups=groups_not_in_post, post_id=post_id, userEmail=session['USERNAME'])

@app.route("/tagGroupWithPost")
def add_group_to_post():
	post_id = request.args.get("id")
	group_id = request.args.get("groupId")
	group_post_dao = GroupPostDao(conn, cur)
	group_post_dao.add_assoc(group_id, post_id, session['USERID'])

	return redirect(url_for('view_post', id=post_id))

@app.route("/deletePersonFromGroup")
def delete_person_from_group():
	person_id = request.args.get("personId")
	group_id = request.args.get("groupId")
	user_id = session['USERID']
	person_group_dao = PersonGroupDao(conn, cur)
	person_group_dao.delete_assoc(person_id, group_id, user_id)
	return redirect(url_for("view_group", id=group_id))

@app.route("/deletePersonFromPost")
def delete_person_from_post():
	person_id = request.args.get("personId")
	post_id = request.args.get("postId")
	user_id = session['USERID']
	person_post_dao = PersonPostDao(conn, cur)
	person_post_dao.delete_assoc(person_id, post_id, user_id)
	return redirect(url_for("view_post", id=post_id))

@app.route("/deleteGroupFromPost")
def delete_group_from_post():
	group_id = request.args.get("groupId")
	post_id = request.args.get("postId")
	user_id = session['USERID']
	group_post_dao = GroupPostDao(conn, cur)
	group_post_dao.delete_assoc(group_id, post_id, user_id)
	return redirect(url_for("view_post", id=post_id))

