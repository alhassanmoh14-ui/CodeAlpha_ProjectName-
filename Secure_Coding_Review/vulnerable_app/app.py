
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# SECURITY ISSUE 1: Hardcoded secret
app.secret_key = "mysecret123"

DATABASE = "users.db"


def get_db():
    return sqlite3.connect(DATABASE)


# SECURITY ISSUE 2: Plain-text password storage
@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")

    db = get_db()
    cursor = db.cursor()

    # SECURITY ISSUE 3: SQL injection
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    cursor.execute(query)

    db.commit()
    db.close()

    return "User registered successfully"


@app.route("/search")
def search():
    username = request.args.get("username", "")

    # SECURITY ISSUE 4: SQL injection
    db = get_db()
    cursor = db.cursor()

    query = f"SELECT username FROM users WHERE username = '{username}'"
    cursor.execute(query)

    results = cursor.fetchall()
    db.close()

    # SECURITY ISSUE 5: Unsafe HTML output (XSS)
    return "<h2>Search results for: " + username + "</h2>" + str(results)


# SECURITY ISSUE 6: Debug mode enabled
if __name__ == "__main__":
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password TEXT
        )
    """)
    db.commit()
    db.close()

    app.run(debug=True)
