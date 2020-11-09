from Objects.entity import *

class PersonDao:

    def to_db(self, person, conn, cur):
        command = f"""INSERT INTO person VALUES ({person.to_str()})"""
        print(command)
        cur.execute(command)
        conn.commit()

class GroupDao:

    def to_db(self, group, conn, cur):
        command = f"""INSERT INTO class VALUES ({group.to_str()})"""
        print(command)
        cur.execute(command)
        conn.commit()


class PostDao:

    def to_db(self, post, conn, cur):
        command = f"""INSERT INTO post VALUES ({post.to_str()})"""
        print(command)
        cur.execute(command)
        conn.commit()

