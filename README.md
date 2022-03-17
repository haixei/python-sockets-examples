![Status: Finished](https://img.shields.io/badge/Status-Finished-%235d6d91)

# Sockets in Python - examples

Example implementations of a socket, made using Python with the socket library and SocketIO. Sockets are endpoints for sending and receiving data across the network and you can learn more about them [here](https://medium.com/swlh/understanding-socket-connections-in-computer-networking-bac304812b5c). 



## About the examples

The starter folder consists of the simplest possible socket example that you can make in Python, start the server and the client and enjoy a simple information exchange. It's useful to learn about what sockets are before building on top of it or diving into the other examples as the comments only describe the code itself. in the "Examples" folder you will find one bigger example with a normal sockets library, it also includes threading. The other example is made with Flask and SocketIO (a library that makes using sockets more friendly). It's a simple chat room where you can pick your username and join rooms. The Chat also logs the messages into a SQLite database.



## Run the projects

This instruction applies to all the folders. Before anything, make sure that you have [pip](https://pypi.org/project/pip/) installed, then proceed to the following steps:

1. Install the required packages

   ```shell
   pip install -r requirements.txt
   ```

2. Next, you will need two terminals, one for your client and one for your server, you can run them like this

   ```shell
   python <file_name>.py
   ```

3. In the case you run the Chat project, feel free to run multiple clients to simulate more users and experiment with the rooms



### Useful resources

- *[What is SocketIO?](https://python-socketio.readthedocs.io/en/latest/intro.html#what-is-socket-io)*
- *[Flask Quickstart](https://flask.palletsprojects.com/en/2.0.x/quickstart/)*
