import os

class Config(object):
    # first, set SECRET_KEY as environment variable in terminal
    # then python will read this key
    SECRET_KEY = os.environ.get('SECRET_KEY')