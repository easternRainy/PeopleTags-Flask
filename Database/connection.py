import psycopg2
import sys
from Database.config_db import *


def connect_db(host=host, port=port, database=database, user=user, password=password):
    try:

       conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
       conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_REPEATABLE_READ)
       cur = conn.cursor()
       return conn, cur

    except:

        print("Failed to connected to database")
        sys.exit()


def disconnect_db(conn, cur):
    conn.close()
    cur.close()
