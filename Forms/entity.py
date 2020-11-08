from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class PersonForm(FlaskForm):
    firstname = StringField('First')
    lastname = StringField('Last')
    email = StringField("Email Address")
    age = StringField("Age")
    job = StringField("Job Title")
    description = StringField("Description")
    submit = SubmitField('Save')

class GroupForm(FlaskForm):
    groupname = StringField("Name")
    description = StringField("Description")
    submit = SubmitField('Save')

class PostForm(FlaskForm):
    post = StringField("Content")
    visibility = BooleanField("Public")
    submit = SubmitField('Save')

class SocialMediaForm(FlaskForm):
    name = StringField("Social Media Name")
    link = StringField("Social Media Link")
    submit = SubmitField('Save')