import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('127.0.0.1', 8080))

conn.listen()

# Always listen for an incoming connection
while True:
    client, address = conn.accept()
    print('Connected to: ', address)

    # Send a message to the client, "b" before the message
    # encodes it to bytes
    client.send(b'You are connected')

    # Close the connection
    client.close()
