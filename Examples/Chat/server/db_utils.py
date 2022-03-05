import sqlite3
from sqlite3 import Error


# Connect to the database
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
        return conn
    except Error as e:
        print(e)
        return None


# Establish a connection
db_conn = create_connection(r"logs.db")


# Create a new table
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


# Create a new message log, requires a tuple of
# (<username:text>, <message:text>, <timestamp:text>)
def create_log(conn, log):
    sql = ''' INSERT INTO logs(username,message,timestamp)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, log)
    conn.commit()
