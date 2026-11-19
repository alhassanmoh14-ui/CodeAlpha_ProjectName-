
import os
import sqlite3
from pathlib import Path

from flask import Flask, request, render_template_string
from werkzeug.security import generate_password_hash

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "users.db"

app = Flask(__name__)

# Secret is supplied through an environment variable.
app.config["SECRET_KEY"] = os.environ.get(
    "FLASK_SECRET_KEY"
) or os.urandom(32)


def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def initialize_database():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)


@app.route("/")
def home():
    return "Secure Coding Review Demo"


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    # Validate user input.
    if not username or len(username) > 50:
        return "Invalid username", 400

    if len(password) < 12 or len(password) > 128:
        return "Password must be 12-128 characters", 400

    # Hash the password before storing it.
    password_hash = generate_password_hash(password)

    try:
        with get_db() as db:
            # Parameterized SQL prevents SQL injection.
            db.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )
    except sqlite3.IntegrityError:
        return "Username already exists", 409

    return "User registered securely", 201


@app.route("/search")
def search():
    username = request.args.get("username", "").strip()

    if len(username) > 50:
        return "Search term too long", 400

    with get_db() as db:
        # User input is passed as a parameter, not SQL code.
        results = db.execute(
            "SELECT username FROM users WHERE username = ?",
            (username,)
        ).fetchall()

    # Flask/Jinja automatically escapes variable output in HTML.
    return render_template_string("""
        <h2>Search Results</h2>
        <ul>
        {% for user in users %}
            <li>{{ user["username"] }}</li>
        {% endfor %}
        </ul>
    """, users=results)


if __name__ == "__main__":
    initialize_database()

    # Debug mode is disabled.
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
