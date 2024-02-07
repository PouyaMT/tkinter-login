import sqlite3
import hashlib


# Function to insert user data into the database
def insert(fullname, username, password):
    # Connect to the SQLite database
    connection = sqlite3.connect("userdata.db")
    cursor = connection.cursor()

    # Create a table if it does not exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY,
        fullname VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    """)

    # Hash the password using SHA-256 algorithm
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Insert user data into the table
    cursor.execute("INSERT INTO userdata (username, password, fullname) VALUES (?, ?, ?)",
                   (username, hashed_password, fullname))

    # Commit changes and close connection
    connection.commit()
