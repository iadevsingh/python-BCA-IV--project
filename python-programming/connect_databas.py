import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("student.db")

# Create a cursor object
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

print("Table created successfully!")

# Commit changes and close connection
conn.commit()
conn.close()