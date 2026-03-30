import sqlite3
import hashlib

def create_user_table():

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
    email TEXT,
    password TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_user(email,password):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    password = hashlib.sha256(password.encode()).hexdigest()

    c.execute("INSERT INTO users VALUES (?,?)",(email,password))

    conn.commit()
    conn.close()


def login_user(email,password):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    password = hashlib.sha256(password.encode()).hexdigest()

    c.execute("SELECT * FROM users WHERE email=? AND password=?",(email,password))

    data = c.fetchone()

    conn.close()

    return data