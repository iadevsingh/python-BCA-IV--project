import sqlite3

# Connect to database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

# ---------------- INSERT ----------------
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
               ("Dev", 20, "BCA"))

# ---------------- UPDATE ----------------
cursor.execute("UPDATE students SET age = ? WHERE name = ?",
               (21, "Dev"))

# ---------------- DELETE ----------------
cursor.execute("DELETE FROM students WHERE name = ?",
               ("Dev",))

# ---------------- SELECT ----------------
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

# Save changes and close
conn.commit()
conn.close()