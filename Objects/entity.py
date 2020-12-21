from Security.account import *
from Forms.entity import *
import datetime

class Person:
    def __init__(self, first_name, last_name, age, job_title, description, email, created_by, id=None):
        if id is None:
            self.id = generate_id()
        else:
            self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job_title = job_title
        self.description = description
        self.email = email
        self.created_by = created_by
        self.image_url = "NULL"

    def to_str(self):
        return f"'{self.id}', '{self.first_name}', '{self.last_name}', {self.age}, '{self.job_title}', '{self.description}', '{self.email}', '{self.created_by}', {self.image_url}"

def PersonFrom_to_Person(form, created_by):
    '''
    create a Person Object from PersonForm
    :param form: PersonFrom
    :return: Person
    '''
    firstname = form.firstname.data
    lastname = form.lastname.data
    email = form.email.data
    age = form.age.data
    job = form.job.data
    description = form.description.data

    person = Person(firstname, lastname, int(age), job, description, email, created_by)
    return person


class Group:
    def __init__(self, name, description, created_by, id=None):
        if id is None:
            self.id = generate_id()
        else:
            self.id = id
        self.name = name
        self.description = description
        self.created_by = created_by
        self.image_url = "NULL"

    def to_str(self):
        return f"'{self.id}', '{self.name}', '{self.description}', '{self.created_by}', {self.image_url}"


def GroupForm_to_Group(form, created_by):
    '''
    create a Group Object from GroupForm
    :param form: GroupFrom
    :return: Group
    '''
    groupname = form.groupname.data
    description = form.description.data

    group = Group(groupname,description, created_by)
    return group


class Post:
    def __init__(self, post, visibility, create_time, created_by, id=None):
        if id is None:
            self.id = generate_id()
        else:
            self.id = id
        self.post = post
        self.visibility = visibility
        self.create_time = create_time
        self.created_by = created_by


    def to_str(self):
        return f"'{self.id}', '{self.post}', '{self.visibility}', '{self.create_time}', '{self.created_by}'"


def PostForm_to_Post(form, created_by):
    '''
    create a Post Object from PostForm
    :param form: PostFrom
    :return: Post
    '''
    post = form.post.data
    visibility = form.visibility.data
    create_time  = str(datetime.date.today())
    post = Post(post, visibility, create_time, created_by)
    return post

