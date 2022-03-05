import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
ADDR = ('127.0.0.1', PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def sendMessage(msg):
    message = msg.encode(FORMAT)
    message_length = len(message)

    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while True:
    newmsg = input()
    sendMessage(newmsg)
    if newmsg == DISCONNECT_MSG:
         exit()