#Write a Python program to connect to an SQLite3 database, create a table, insert data, and
#fetch data.


import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table named 'users'
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    city TEXT NOT NULL
)
''')

# Insert some data into the 'users' table
cursor.execute("INSERT INTO users (name, age, city) VALUES (?, ?, ?)", ('Amit', 28, 'Mumbai'))
cursor.execute("INSERT INTO users (name, age, city) VALUES (?, ?, ?)", ('Sneha', 24, 'Delhi'))
cursor.execute("INSERT INTO users (name, age, city) VALUES (?, ?, ?)", ('Rahul', 30, 'Bangalore'))

# Commit the changes to the database
conn.commit()

# Fetch all data from the 'users' table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print the fetched data
print("Data in users table:")
for row in rows:
    print(row)

# Close the connection
conn.close()

