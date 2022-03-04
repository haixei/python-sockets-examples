import socket

# Create a socket over the TCP
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the localhost on port 8080
conn.connect(('127.0.0.1', 8080))

# Receive a message that is max 1024 bytes
message = conn.recv(1024)

# Close the connection
conn.close()

# Decode the message from bytes
print(message.decode())
