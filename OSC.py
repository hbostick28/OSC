import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Successfully connected to database.")
    except Error as e:
        print(e)

    return conn

#function to create a table
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        c.close()
    except Error as e:
        print(e)

#function to insert data into a table
def insert_data(conn, insert_data_sql):
    try:
        c = conn.cursor()
        c.execute(insert_data_sql)
        conn.commit()
        print("Successfully populated table with data.\n")
        c.close()
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

    
    #populate tables with data
##    insert_query1 = """INSERT INTO household_items (name, description, price)
##    VALUES ('Paper Towels', 'Bounty paper towels', 3.50)"""
##    insert_query2 = """INSERT INTO household_items (name, description, price)
##    VALUES ('Vacuum', 'Dyson bagless upright vacuum, black', 54.00)"""
##    insert_query3 = """INSERT INTO household_items (name, description, price)
##    VALUES ('Mini-fridge', '1.7 cubic ft single door mini fridge, black', 79.00)"""
##    insert_query4 = """INSERT INTO household_items (name, description, price)
##    VALUES ('Curtains', 'Mainstays textured solid curtain panel, black', 5.88)"""
##    insert_query5 = """INSERT INTO household_items (name, description, price)
##    VALUES ('Table', '6ft centerfold table, white', 42.00)"""

    
    
    #create database connection
    conn = create_connection(database)
    c = conn.cursor()

    #create table
    if conn is not None:
        create_table(conn, household_items_table)
        create_table(conn, books_table)
        create_table(conn, toys_table)
        create_table(conn, small_electronics_table)
    else:
        print("Error! Cannot create the database connection.")

##    if conn is not None:
##        insert_data(conn, insert_query1)
##        insert_data(conn, insert_query2)
##        insert_data(conn, insert_query3)
##        insert_data(conn, insert_query4)
##        insert_data(conn, insert_query5)
##    else:
##        print("Failed to populate table with data.\n")

main()
