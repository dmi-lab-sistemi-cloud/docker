import socket
import os

# get server port from envs (8080 by default)
PORT = os.environ.get('PORT', '8080')

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to all interfaces, and a well-known port
serversocket.bind(('', int(PORT)))
# become a server socket
serversocket.listen()

while True:
    print("Waiting for connections on port " + PORT + ":")
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket
    with clientsocket:
        print('Client', address)
        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            print("> " + str(data))
            clientsocket.sendall(b'ECHO ' + data)