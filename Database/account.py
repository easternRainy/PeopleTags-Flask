from Objects.account import *
from Security.account import *

class UserDao:
    def __init__(self, conn, cur):
        self.table = "my_user"
        self.conn = conn
        self.cur = cur

    def to_db(self, user):
        command = f"""INSERT INTO {self.table} VALUES ({user.to_str()})"""
        self.cur.execute(command)
        self.conn.commit()

    def check(self, username, password):
        command = f"""SELECT * FROM {self.table} WHERE my_username='{username}'"""
        self.cur.execute(command)
        records = self.cur.fetchall()
        if len(records) != 1:
            return False
        else:
            record = records[0]
            username = record[1]
            hash = record[2]
            salt = record[3]
            check = verify_password(password, salt, hash)

            return check

    def check_exist(self, username):
        command = f"""SELECT my_username FROM {self.table} WHERE my_username='{username}'"""
        self.cur.execute(command)
        records = self.cur.fetchall()

        return len(records) > 0;

    def get_user_id(self, username):
        command = f"""SELECT id FROM {self.table} WHERE my_username = '{username}'"""
        self.cur.execute(command)
        records = self.cur.fetchall()

        return records[0][0]