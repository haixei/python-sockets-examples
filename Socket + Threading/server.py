import socket
import threading

# Set the maximum size of the message the socket will accept, we
# set it to 64 bytes
HEADER = 64

# Set the port on which the socket will run
PORT = 5050

# Get the IP address of the host
SERVER = socket.gethostbyname(socket.gethostname())

# Set the adress and the encoding on messages
ADDR = ('127.0.0.1', PORT)
FORMAT = "utf-8"

# If client send this message, the server will disconnect
DISCONNECT_MSG = "!DISCONNECT"

# Create the socket endpoint and bind to the address (ip, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, )
server.bind(ADDR)


# This function will handle our socket connection
def handle_client(conn, addr):
    print(f"{addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Message received.".encode(FORMAT))

    conn.close()


def server_start():
    # Start listening to upcoming data
    server.listen()
    print(f"Server is listening on: {SERVER}")
    while True:
        # "conn" refers to the connection between the server and the client that was
        # established, "addr" is the address of the client
        conn, addr = server.accept()

        # We create a new thread for our connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active Connections: {threading.activeCount() - 1}")


print("Server is starting..")
server_start()
