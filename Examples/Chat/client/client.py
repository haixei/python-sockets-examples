import socketio
from termcolor import cprint

sio = socketio.Client()


@sio.on('welcome')
def welcome():
    print('Connection established.')


# Messages
@sio.on('receive_message')
def receive(data):
    if data['username'] == client_username:
        cprint('Me: ' + data['msg'], 'green')
    else:
        cprint(data['username'] + ': ' + data['msg'], 'yellow')


# Rooms
@sio.on('room_welcome')
def receive(data):
    room = data['room']
    username = data['username']
    print(f'Welcome to the room {room} {username}!')


@sio.on('room_goodbye')
def receive():
    print('Disconnected from the room.')


# The first thing user will see after launching the client
def start_menu():
    cprint('Choose your username: ', 'blue')
    username = input()

    if username == '':
        cprint('Username cannot be empty!', 'red')
        start_menu()

    cprint('Room name: ')
    room = input()

    # Set the defaults
    if room == '':
        cprint('Room undefined, it will be set to "general".', 'blue')
        room = 'general'

    return username, room


# Connect the socket
sio.connect('http://localhost:5050')

# Set the username
client_username, client_room = start_menu()

# Join the room
sio.emit('join_room', {'room': client_room, 'username': client_username})

while True:
    # Let the user send messages
    msg = input()
    if msg != '':
        sio.emit('send_message', {'msg': msg, 'room': client_room, 'username': client_username})
    else:
        cprint('Message cannot be empty!', 'red')
