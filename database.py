import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
name TEXT,
phone TEXT
)
""")

conn.commit()

def check_status(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()
    return user

def add_user(update):
    phone = update.message.contact.phone_number
    user = update.message.from_user

    cursor.execute(
        "INSERT INTO users (user_id,name,phone) VALUES (?,?,?)",
        (user.id, user.first_name, phone)
    )

    conn.commit()