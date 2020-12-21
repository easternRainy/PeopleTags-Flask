from Security.account import *

class User:

    def __init__(self, username, password, id=None, salt=None):
        if id is None:
            self.id = generate_id()
        else:
            self.id = id

        self.username = username

        if salt is None:
            self.salt = generate_salt()
        else:
            self.salt = salt

        self.password = hash_password(password, self.salt)

    def to_str(self):

        return f"'{self.id}', '{self.username}', '{self.password}', '{self.salt}'"

    def get_username(self):
        return self.username

    def get_id(self):
        return self.id

def RegisterForm_to_User(form):
    '''
    create a User Object from RegisterForm
    :param form: RegisterFrom
    :return: User
    '''
    username = form.username.data
    password = form.password.data

    user = User(username, password)
    return user