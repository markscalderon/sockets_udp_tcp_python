# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:08:45 2017

@author: mcalderon
"""

import socket


 
# define socket address
IP = '127.0.0.1'  # ip of the server we want to connect to
PORT = 10000  # port used for communicating with the server
BUFFER_SIZE = 1024 #buffer size used when receiving data
# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully.")

#connect to server
s.connect((IP, PORT))

print("Established connection with the server")
msg = 'Hello server '
s.send(msg.encode("utf-8"))

#receive data from server
data = s.recv(BUFFER_SIZE)
print("The message received from the server %s", data )