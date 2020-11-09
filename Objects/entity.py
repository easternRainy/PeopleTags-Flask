from Security.utils import generate_id
from Forms.entity import *

class Person:
    def __init__(self, first_name, last_name, age, job_title, description, email, id=None):
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
        self.created_by = "NULL"
        self.image_url = "NULL"

    def to_str(self):
        return f"'{self.id}', '{self.first_name}', '{self.last_name}', {self.age}, '{self.job_title}', '{self.description}', '{self.email}', {self.created_by}, {self.image_url}"

def PersonFrom_to_Person(form):
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

    person = Person(firstname, lastname, int(age), job, description, email)
    return person


class Group:
    def __init__(self, name, description, id=None):
        if id is None:
            self.id = generate_id()
        else:
            self.id = id
        self.name = name
        self.description = description
        self.created_by = "NULL"
        self.image_url = "NULL"

    def to_str(self):
        return f"'{self.id}', '{self.name}', '{self.description}', {self.created_by}, {self.image_url}"


def GroupForm_to_Group(form):
    '''
    create a Group Object from GroupForm
    :param form: GroupFrom
    :return: Group
    '''
    groupname = form.groupname.data
    description = form.description.data

    group = Group(groupname,description)
    return group


class Post:
    def __init__(self, name, description, id=None):
        if id is None:
            self.id = generate_id()
        else:
            self.id = id
        self.name = name
        self.description = description
        self.created_by = "NULL"
        self.image_url = "NULL"

    def to_str(self):
        return f"'{self.id}', '{self.name}', '{self.description}', {self.created_by}, {self.image_url}"


def PostForm_to_Post(form):
    '''
    create a Group Object from GroupForm
    :param form: GroupFrom
    :return: Group
    '''
    name = form.description.data
    description = form.description.data

    group = Group(name, description)
    return group


