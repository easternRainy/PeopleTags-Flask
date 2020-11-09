import hashlib
import numpy as np
import time
import binascii
from Security.security_config import *

def generate_id():
    '''
    generate userId, groupId, personId,...
    :return: str
    '''
    time_stamp = str(time.time()).encode(encode_method)
    salt = str(np.random.rand()).encode(encode_method)
    m = hashlib.sha256()
    m.update(time_stamp)
    m.update(salt)

    print(m.hexdigest())
    print(m.digest().hex() == m.hexdigest())

    return m.hexdigest()

def hash_password(password, salt, n):
    '''
    to securely save users' passwords, we need to hash them for n times
    :param password: the password to be hashed and saved
    :param salt: random number
    :param n: n times of hash
    :return: hashed password
    '''
    assert n >= 10
    b_password = password.encode(encode_method)
    b_salt = salt.encode(encode_method)
    tmp = b_password + b_salt

    for i in range(n):
        m = hashlib.sha256()
        m.update(tmp)
        tmp = m.digest()

    return tmp.hex()

def verify_password(password, salt, n, hash):
    '''
    verify if password is right
    hashing password with salt for n times, check if the hash maches
    :param password: password to be verified
    :param salt: salt, usually from database
    :param n: times of hash
    :param hash: hash value from database. this hash is used to compare
    :return: if the result matches
    '''
    password_hash = hash_password(password, salt, n)
    return password_hash == hash


def update_hash_times(old_password_hash, new_n, old_n):
    '''
    for update hash times
    update the password hash from old_n times, to new_n times

    :return: new hash
    '''

    assert new_n > old_n
    diff = new_n - old_n

    tmp = bytearray.fromhex(old_password_hash)
    for i in range(diff):
        m = hashlib.sha256()
        m.update(tmp)
        tmp = m.digest()

    return tmp.hex()


