from Objects.entity import *

class SingleDao:

    def __init__(self, conn, cur):
        self.table = ""
        self.conn = conn
        self.cur = cur

    def to_db(self, object):
        command = f"""INSERT INTO {self.table} VALUES ({object.to_str()})"""
        self.cur.execute(command)
        self.conn.commit()

    def entity_to_object(self, record):
        pass

    def entities_to_objects(self, records):
        return [self.entity_to_object(record) for record in records]

    def list_by_user(self, user_id):
        command = f"""SELECT * FROM {self.table} WHERE created_by = '{user_id}'"""
        self.cur.execute(command)
        records = self.cur.fetchall()
        return records

    def select_by_id(self, id):
        command = f"""SELECT * FROM {self.table} WHERE id='{id}'"""
        self.cur.execute(command)
        records = self.cur.fetchall()
        if len(records) != 1:
            return None
        record = records[0]
        return self.entity_to_object(record)

    def delete(self, id):
        command = f"""DELETE FROM {self.table} WHERE id = '{id}'"""
        self.cur.execute(command)
        self.conn.commit()

class PersonDao(SingleDao):

    def __init__(self, conn, cur):
        super().__init__(conn, cur)
        self.table = "person"

    def entity_to_object(self, record):
        id, first_name, last_name, age, job_title,description,email, created_by, image_url = record
        person = Person(first_name, last_name, age, job_title, description, email, created_by, id=id)
        return person


class GroupDao(SingleDao):

    def __init__(self, conn, cur):
        super().__init__(conn, cur)
        self.table = "class"

    def entity_to_object(self, record):
        id = record[0]
        name = record[1]
        description = record[2]
        created_by = record[3]

        group = Group(name, description, created_by, id=id)

        return group


class PostDao(SingleDao):

    def __init__(self, conn, cur):
        super().__init__(conn, cur)
        self.table = "post"

    def entity_to_object(self, record):
        id = record[0]
        post_content = record[1]
        visibility = record[2]
        create_time = record[3]
        created_by = record[4]

        post = Post(post_content, visibility, create_time, created_by, id=id)

        return post

    def select_public(self):
        command = f"""SELECT * FROM {self.table} WHERE visibility = 'True'"""
        self.cur.execute(command)
        records = self.cur.fetchall()
        public_posts = self.entities_to_objects(records)
        return public_posts



