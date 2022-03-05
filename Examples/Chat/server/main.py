from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room
from db_utils import create_log, db_conn
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
sio = SocketIO(app)


def messageReceived(methods=['GET', 'POST']):
    print('Connected to a client.')


@sio.on('connect')
def connected():
    sio.emit('welcome', callback=messageReceived)


@sio.on('send_message')
def send_message(data):
    # Create a message log
    timestamp = str(datetime.datetime.utcnow())
    log_tuple = (data['username'], data['msg'], timestamp)
    create_log(db_conn, log_tuple)

    # Send message to every user in the room
    sio.emit('receive_message', data={'msg': data['msg'], 'username': data['username']}, to=data['room'])


# Join and leave chat rooms
@sio.on('join_room')
def handle_join_room(data):
    app.logger.info("User joined the room.")
    join_room(data['room'])
    # Emit event to the client so new user can be displayed on the list
    sio.emit('room_welcome', to=data['room'], data={'room': data['room'], 'username': data['username']})


@sio.on('leave_room')
def leave_room(data):
    leave_room(data['room'])
    # Emit event to the client so new user can be displayed on the list
    sio.emit('room_goodbye')


if __name__ == '__main__':
    sio.run(app, debug=True, port=5050)
