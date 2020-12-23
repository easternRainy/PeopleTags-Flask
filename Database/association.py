from Database.entity import *
from Security.account import *

class PersonGroupDao:

    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur
        self.personDao = PersonDao()
        self.groupDao = GroupDao()

    def get_persons_in_group(self, cur, id, user_id):
        command = f"""
                    SELECT * 
                    FROM person
                    WHERE 
                        person.created_by = '{user_id}' AND

                        person.id IN (
                             SELECT DISTINCT person FROM person_class_assoc
                             WHERE class = '{id}' AND created_by = '{user_id}'
                        )    
                    """
        self.cur.execute(command)
        records = self.cur.fetchall()
        persons = self.personDao.entities_to_objects(records)

        return persons


    def get_persons_not_in_group(self, group_id, user_id):
        command = f"""
                    SELECT * 
                    FROM person
                    WHERE 
                        person.created_by = '{user_id}' AND

                        person.id NOT IN (
                             SELECT DISTINCT person FROM person_class_assoc
                             WHERE class = '{group_id}' AND created_by = '{user_id}'
                        )    
                    """
        self.cur.execute(command)
        records = self.cur.fetchall()
        persons = self.personDao.entities_to_objects(records)

        return persons

    def add_assoc(self, person_id, group_id, user_id):
        assoc_id = generate_id()
        command = f"""INSERT INTO person_class_assoc VALUES ('{assoc_id}', '{person_id}', '{group_id}', '{user_id}')"""
        # print(command)
        self.cur.execute(command)
        self.conn.commit()

