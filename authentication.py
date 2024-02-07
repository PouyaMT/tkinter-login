import socket
import hashlib
import sqlite3


# Function to authenticate a client using username and password
def authenticate_client(username, password):
    # Hash the password using SHA-256 algorithm
    password = hashlib.sha256(password.encode()).hexdigest()

    # Connect to the SQLite database
    connection = sqlite3.connect("userdata.db")
    cursor = connection.cursor()

    # Execute a query to check if the username and password match
    cursor.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))

    # If there is a match, return "Success", otherwise return "Failed"
    if cursor.fetchall():
        return "Success"
    else:
        return "Failed"


# Function to check if a username already exists
def check(username):
    # Connect to the SQLite database
    connection = sqlite3.connect("userdata.db")
    cursor = connection.cursor()

    # Execute a query to check if the username exists
    cursor.execute("SELECT * FROM userdata WHERE username = ?", (username,))

    # If the username exists, return "Success", otherwise return "Failed"
    if cursor.fetchall():
        return "Success"
    else:
        return "Failed"


# Function to handle the connection between client and server
def handle_connection(client):
    # Send a message to the client to enter username
    client.send("Username: ".encode())
    username = client.recv(1024).decode()

    # Send a message to the client to enter password
    client.send("Password: ".encode())
    password = client.recv(1024).decode()

    # Authenticate the client based on entered credentials
    result = authenticate_client(username, password)

    # Send the authentication result to the client
    client.send(result.encode())


# Function to interact with the server as a client
def client(username, password):
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client.connect(("localhost", 9999))

    # Receive initial message from the server
    message = client.recv(1024).decode()

    # Send username to the server
    client.send(username.encode())

    # Receive message from the server
    message = client.recv(1024).decode()

    # Send password to the server
    client.send(password.encode())

    # Receive and return the final authentication result from the server
    return client.recv(1024).decode()
