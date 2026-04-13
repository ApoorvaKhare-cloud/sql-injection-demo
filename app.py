import bcrypt
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    mode = request.form['mode']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    if mode == "vulnerable":
        # 😈 Vulnerable query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchone()

        conn.close()

        if result:
            return "Login Successful (Vulnerable Mode) 😈"
        else:
            return "Login Failed ❌"

    else:
        # 🛡️ Secure query with hashing
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        conn.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[2]):
            return "Login Successful (Secure Mode) 🛡️"
        else:
            return "Login Failed ❌"


if __name__ == '__main__':
    app.run(debug=True)