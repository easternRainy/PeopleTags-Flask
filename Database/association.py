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


    def get_persons_not_in_group(self, id, user_id):
        return self.get_A_not_in_B(id, user_id)



