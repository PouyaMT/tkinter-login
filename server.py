import socket
import threading
from authentication import handle_connection

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server.bind(("localhost", 9999))

# Listen for incoming connections
server.listen()

# Accept connections and start a new thread for each connection
while True:
    # Accept a new connection
    client, addr = server.accept()

    # Start a new thread to handle the connection
    threading.Thread(target=handle_connection, args=(client,)).start()
