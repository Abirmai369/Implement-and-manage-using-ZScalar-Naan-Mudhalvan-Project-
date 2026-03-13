
import sqlite3

def validate_user(username,password):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    user=cur.fetchone()

    conn.close()
    return user is not None
