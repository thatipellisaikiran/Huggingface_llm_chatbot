import sqlite3

conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats(
id INTEGER PRIMARY KEY AUTOINCREMENT,
question TEXT,
answer TEXT
)
""")

def save_chat(question,answer):
    cursor.execute(
        "INSERT INTO chats(question,answer) VALUES (?,?)",
        (question,answer)
    )
    conn.commit()

def load_chats():
    cursor.execute("SELECT * FROM chats ORDER BY id DESC")
    return cursor.fetchall()