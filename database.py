import sqlite3

def create_db():
    conn = sqlite3.connect("study.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        content TEXT
    )
    """)

    conn.commit()
    conn.close()

create_db()
