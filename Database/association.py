from Database.entity import *
from Security.account import *

class AssocDao:

    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur
        self.daoA = None
        self.daoB = None
        self.tableA = ""
        self.tableB = ""
        self.assoc_table = ""

    def get_A_in_B(self, id, user_id):
        command = f"""
                    SELECT * 
                    FROM {self.tableA}
                    WHERE 
                        {self.tableA}.created_by = '{user_id}' AND
    
                        {self.tableA}.id IN (
                             SELECT DISTINCT {self.tableA} FROM {self.assoc_table}
                             WHERE {self.tableB} = '{id}' AND created_by = '{user_id}'
                        )    
                    """
        self.cur.execute(command)
        records = self.cur.fetchall()
        A_s = self.daoA.entities_to_objects(records)

        return A_s

    def get_B_in_A(self, id, user_id):
        command = f"""
                    SELECT * 
                    FROM {self.tableB}
                    WHERE 
                        {self.tableB}.created_by = '{user_id}' AND

                        {self.tableB}.id IN (
                             SELECT DISTINCT {self.tableB} FROM {self.assoc_table}
                             WHERE {self.tableA} = '{id}' AND created_by = '{user_id}'
                        )    
                    """
        # print(command)
        self.cur.execute(command)
        records = self.cur.fetchall()
        B_s = self.daoB.entities_to_objects(records)

        return B_s


    def get_A_not_in_B(self, id, user_id):
        command = f"""
                    SELECT * 
                    FROM {self.tableA}
                    WHERE 
                        {self.tableA}.created_by = '{user_id}' AND

                        {self.tableA}.id NOT IN (
                             SELECT DISTINCT {self.tableA} FROM {self.assoc_table}
                             WHERE {self.tableB} = '{id}' AND created_by = '{user_id}'
                        )    
                    """
        self.cur.execute(command)
        records = self.cur.fetchall()
        A_s = self.daoA.entities_to_objects(records)

        return A_s

    def add_assoc(self, A_id, B_id, user_id):
        assoc_id = generate_id()
        command = f"""INSERT INTO {self.assoc_table} VALUES ('{assoc_id}', '{A_id}', '{B_id}', '{user_id}')"""
        # print(command)
        self.cur.execute(command)
        self.conn.commit()

    def delete_assoc(self, A_id, B_id, user_id):
        command = f"""DELETE FROM {self.assoc_table} WHERE {self.tableA} = '{A_id}' AND {self.tableB} = '{B_id}' AND created_by = '{user_id}'"""
        self.cur.execute(command)
        self.conn.commit()

class PersonGroupDao(AssocDao):

    def __init__(self, conn, cur):
        super().__init__(conn, cur)
        self.daoA = PersonDao(conn, cur)
        self.daoB = GroupDao(conn, cur)
        self.tableA = "person"
        self.tableB = "class"
        self.assoc_table = "person_class_assoc"



    def get_persons_in_group(self, id, user_id):
        return self.get_A_in_B(id, user_id)

    def get_groups_by_person(self, id, user_id):
        return self.get_B_in_A(id, user_id)


    def get_persons_not_in_group(self, id, user_id):
        return self.get_A_not_in_B(id, user_id)




class PersonPostDao(AssocDao):

    def __init__(self, conn, cur):
        super().__init__(conn, cur)
        self.daoA = PersonDao(conn, cur)
        self.daoB = PostDao(conn, cur)
        self.tableA = "person"
        self.tableB = "post"
        self.assoc_table = "person_post_assoc"

    def get_persons_in_post(self, id, user_id):
        return self.get_A_in_B(id, user_id)

    def get_posts_by_person(self, id, user_id):
        return self.get_B_in_A(id, user_id)


    def get_persons_not_in_post(self, id, user_id):
        return self.get_A_not_in_B(id, user_id)


class GroupPostDao(AssocDao):

    def __init__(self, conn, cur):
        super().__init__(conn, cur)
        self.daoA = GroupDao(conn, cur)
        self.daoB = PostDao(conn, cur)
        self.tableA = "class"
        self.tableB = "post"
        self.assoc_table = "class_post_assoc"

    def get_groups_in_post(self, id, user_id):
        return self.get_A_in_B(id, user_id)

    def get_posts_by_group(self, id, user_id):
        return self.get_B_in_A(id, user_id)

    def get_groups_not_in_post(self, id, user_id):
        return self.get_A_not_in_B(id, user_id)


class PersonSocialMediaDao(AssocDao):

    def __init__(self, conn, cur):
        super().__init__(conn, cur)
        self.daoA = PersonDao(conn, cur)
        self.daoB = SocialMediaDao(conn, cur)
        self.tableA = "person"
        self.tableB = "social_media"
        self.assoc_table = "person_social_media_assoc"

    def get_social_medias_by_person(self, id, user_id):
        return self.get_B_in_A(id, user_id)