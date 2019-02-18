import json
import psycopg2

from application.util import config

def connect():
    db_conf = config.get_db_config()
    connect_string = "dbname=%s user=%s password=%s host=%s" % (db_conf['dbname'], db_conf['user'], db_conf['password'], db_conf['host'])
    conn = psycopg2.connect(connect_string)
    return conn