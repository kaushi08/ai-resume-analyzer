import sqlite3

conn = sqlite3.connect("resume_data.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    score REAL
)
''')

conn.commit()


def save_result(filename, score):
    cursor.execute(
        "INSERT INTO analysis (filename, score) VALUES (?, ?)",
        (filename, score)
    )

    conn.commit()



def get_results():
    cursor.execute("SELECT * FROM analysis")
    return cursor.fetchall()