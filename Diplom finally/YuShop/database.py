import sqlite3
from handlers.taskhandler import *

connection = sqlite3.connect('filesdb/database.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT); ")
cursor.execute("CREATE TABLE IF NOT EXISTS block(id INT); ")

def add(id):
    if (id,) in get_id(): return
    cursor.execute(f"INSERT INTO users VALUES({id});")
    connection.commit()

def get_users():
    s = cursor.execute("SELECT * FROM users;").fetchall()
    connection.commit()
    return s

def count():
    s = cursor.execute("SELECT COUNT(*) FROM users;").fetchone()
    connection.commit()
    return s[0]

def get_id():
    s = cursor.execute("SELECT id FROM users;").fetchall()
    connection.commit()
    return s

def check_block(id):
    s = cursor.execute("SELECT * FROM block; ").fetchall()
    connection.commit()
    return (id,) in s

def block(id):
    cursor.execute(f"INSERT INTO block VALUES({id}); ").fetchall()
    connection.commit()

def delete(id):
    cursor.execute(f"DELETE FROM block WHERE id = {id}; ").fetchall()
    connection.commit()
