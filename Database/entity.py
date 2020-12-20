from Objects.entity import *

class PersonDao:

    def to_db(self, person, conn, cur):
        command = f"""INSERT INTO person VALUES ({person.to_str()})"""
        cur.execute(command)
        conn.commit()

    def entity_to_object(self, record):
        id, first_name, last_name, age, job_title,description,email, created_by, image_url = record
        person = Person(first_name, last_name, age, job_title, description, email, id=id)
        return person

    def entities_to_objects(self, records):
        return [self.entity_to_object(record) for record in records]

    def list_by_user(self, cur):
        command = f"""SELECT * FROM person"""
        cur.execute(command)
        records = cur.fetchall()
        return records

    def select_by_id(self, cur, id):
        command = f"""SELECT * FROM person WHERE id='{id}'"""
        cur.execute(command)
        records = cur.fetchall()
        if len(records) != 1:
            return None
        record = records[0]
        return self.entity_to_object(record)

class GroupDao:

    def to_db(self, group, conn, cur):
        command = f"""INSERT INTO class VALUES ({group.to_str()})"""
        cur.execute(command)
        conn.commit()

    def entity_to_object(self, record):
        id = record[0]
        name = record[1]
        description = record[2]

        group = Group(name, description, id=id)

        return group

    def entities_to_objects(self, records):
        return [self.entity_to_object(record) for record in records]

    def list_by_user(self, cur):
        command = f"""SELECT * FROM class"""
        cur.execute(command)
        records = cur.fetchall()
        return records

    def select_by_id(self, cur, id):
        command = f"""SELECT * FROM class WHERE id='{id}'"""
        cur.execute(command)
        records = cur.fetchall()
        if len(records) != 1:
            return None
        record = records[0]
        return self.entity_to_object(record)



class PostDao:

    def to_db(self, post, conn, cur):
        command = f"""INSERT INTO post VALUES ({post.to_str()})"""
        cur.execute(command)
        conn.commit()

    def entity_to_object(self, record):
        id = record[0]
        post_content = record[1]
        visibility = record[2]

        post = Post(post_content, visibility, id=id)

        return post

    def entities_to_objects(self, records):
        return [self.entity_to_object(record) for record in records]

    def list_by_user(self, cur):
        command = f"""SELECT * FROM post"""
        cur.execute(command)
        records = cur.fetchall()
        return records

    def select_by_id(self, cur, id):
        command = f"""SELECT * FROM post WHERE id='{id}'"""
        cur.execute(command)
        records = cur.fetchall()
        if len(records) != 1:
            return None
        record = records[0]
        return self.entity_to_object(record)

    def select_public(self, cur):
        command = f"""SELECT * FROM post WHERE visibility = 'True'"""
        cur.execute(command)
        records = cur.fetchall()
        public_posts = self.entities_to_objects(records)
        return public_posts


