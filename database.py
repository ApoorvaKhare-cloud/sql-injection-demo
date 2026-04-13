import sqlite3
import bcrypt

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password BLOB
)
''')

# Hash password
hashed = bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt())

# Insert user with hashed password
cursor.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    ('admin', hashed)
)

conn.commit()
conn.close()

print("Database created with hashed password!")