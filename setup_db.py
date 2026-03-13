
import sqlite3

conn=sqlite3.connect("database.db")
cur=conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT
)
''')

cur.execute("INSERT INTO users (username,password) VALUES ('admin','admin123')")
cur.execute("INSERT INTO users (username,password) VALUES ('user1','1234')")

conn.commit()
conn.close()

print("Database created successfully")
