import sqlite3
import os


# Buat database tugas
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

print("Database digunakan pada:", os.path.abspath('tasks.db'))

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    deadline TEXT,
    priority TEXT,
    status TEXT DEFAULT 'Belum Selesai'
)
''')
conn.commit()
conn.close()
