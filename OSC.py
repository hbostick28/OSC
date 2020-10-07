import sqlite3



def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("SQLite Version: ", sqlite3.version)
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    
def main():
    database = (r"C:\sqlite\db\osc_system.db")

    #Create the inventory category tables
    household_items_table = """CREATE TABLE IF NOT EXISTS household_items (
        name TEXT PRIMARY KEY,
        description TEXT NOT NULL,
        price REAL NOT NULL
    );"""

    books_table = """CREATE TABLE IF NOT EXISTS books (
        name TEXT PRIMARY KEY,
        description TEXT NOT NULL,
        price REAL NOT NULL
    );"""

    toys_table = """CREATE TABLE IF NOT EXISTS toys (
        name TEXT PRIMARY KEY,
        description TEXT NOT NULL,
        price REAL NOT NULL
    );"""

    small_electronics_table = """CREATE TABLE IF NOT EXISTS small_electronics_items (
        name TEXT PRIMARY KEY,
        description TEXT NOT NULL,
        price REAL NOT NULL
    );"""
    #create database connection
    conn = create_connection(database)

    #create table
    if conn is not None:
        create_table(conn, household_items_table)
        create_table(conn, books_table)
        create_table(conn, toys_table)
        create_table(conn, small_electronics_table)
    else:
        print("Error! Cannot create the database connection.")

main()
