import socket
import os
import time

# get server port from envs (8080 by default)
HOST = os.environ.get('HOST', '127.0.0.1') 
PORT = os.environ.get('PORT', '8080')

while True:
    try:
        print("Connecting to {}:{}".format(HOST, PORT))
        # create an INET, STREAMing socket
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to server host
        clientsocket.connect((HOST, int(PORT)))
        # if connected
        break
    except socket.error:
        print("Connection refused, try again in 5s:")
        time.sleep(5)

# send message
clientsocket.sendall(b'Hello, world')

# receive echo
echo = clientsocket.recv(1024)
print("> " + str(echo))