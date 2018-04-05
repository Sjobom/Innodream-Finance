import json

import psycopg2

def connect():
    with open("../../config/db_config.json", "r") as db_config_file:
        db_conf = json.load(db_config_file)
        connect_string = "dbname=%s user=%s password=%s host=%s" % (db_conf['dbname'], db_conf['user'], db_conf['password'], db_conf['host'])
        conn = psycopg2.connect(connect_string)
        return conn