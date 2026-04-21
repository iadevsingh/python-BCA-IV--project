import sqlite3

# Connect to database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY,
    name TEXT,
    balance INTEGER
)
""")

# Insert sample data
cursor.execute("INSERT OR IGNORE INTO accounts VALUES (1, 'Dev', 1000)")
cursor.execute("INSERT OR IGNORE INTO accounts VALUES (2, 'Ram', 1000)")

try:
    # -------- TRANSACTION START --------
    
    # Deduct from Dev
    cursor.execute("UPDATE accounts SET balance = balance - 500 WHERE id = 1")
    
    # Simulate error (uncomment to test rollback)
    # x = 10 / 0
    
    # Add to Ram
    cursor.execute("UPDATE accounts SET balance = balance + 500 WHERE id = 2")
    
    # Commit if all operations succeed
    conn.commit()
    print("Transaction successful! Changes committed.")

except Exception as e:
    # Rollback if any error occurs
    conn.rollback()
    print("Transaction failed! Changes rolled back.")
    print("Error:", e)

# Display final data
cursor.execute("SELECT * FROM accounts")
rows = cursor.fetchall()

print("\nFinal Records:")
for row in rows:
    print(row)

# Close connection
conn.close()