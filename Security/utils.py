import hashlib
import numpy as np
import time

def generate_id():
    '''
    generate userId, groupId, personId,...
    :return: str
    '''
    time_stamp = str(time.time()).encode('ascii')
    salt = str(np.random.rand()).encode('ascii')
    m = hashlib.sha256()
    m.update(time_stamp)
    m.update(salt)

    return m.hexdigest()

