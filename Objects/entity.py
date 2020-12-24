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

    def str_on_update(self):
        '''
        for update, insert int UPDATE table SET {  } WHERE ...

        :return:
        '''
        return f"""first_name = '{self.first_name}', 
                   last_name = '{self.last_name}', 
                   age = {self.age}, 
                   job_title = '{self.job_title}', 
                   description = '{self.description}', 
                   email = '{self.email}',
                   created_by = '{self.created_by}',
                   image_url = '{self.image_url}'
                """

    def to_form(self):
        form = PersonForm()
        form.firstname.data = self.first_name
        form.lastname.data = self.last_name
        form.age.data = self.age
        form.job.data = self.job_title
        form.description.data = self.description
        form.email.data = self.email
        return form

def PersonFrom_to_Person(form, created_by, id=None):
    '''
    create a Person Object from PersonForm
    :param form: PersonFrom
    :return: Person
    '''
    firstname = form.firstname.data
    lastname = form.lastname.data
    email = form.email.data
    age = form.age.data

    try:
        age = int(age)
    except:
        age = -1
    job = form.job.data
    description = form.description.data

    person = Person(firstname, lastname, int(age), job, description, email, created_by, id=id)
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

    def str_on_update(self):
        return f"""
                name = '{self.name}',
                description = '{self.description}',
                created_by = '{self.created_by}',
                image_url = '{self.image_url}'
                """

    def to_form(self):
        form = GroupForm()
        form.groupname.data = self.name
        form.description.data = self.description

        return form


def GroupForm_to_Group(form, created_by, id=None):
    '''
    create a Group Object from GroupForm
    :param form: GroupFrom
    :return: Group
    '''
    groupname = form.groupname.data
    description = form.description.data

    group = Group(groupname,description, created_by, id=id)
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

class SocialMedia:
    def __init__(self, social_media_name, link, created_by, id=None):
        if id is None:
            self.id = generate_id()
        else:
            self.id = id
        self.social_media_name = social_media_name
        self.link = link
        self.created_by = created_by

    def to_str(self):
        return f"'{self.id}', '{self.social_media_name}', '{self.link}', '{self.created_by}'"

    def get_id(self):
        return self.id

def SocialMediaForm_to_SocialMedia(form, created_by):
    name = form.name.data
    link = form.link.data
    social_media = SocialMedia(name, link, created_by)
    return social_media