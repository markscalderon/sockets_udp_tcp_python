# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:07:07 2017

@author: mcalderon
"""

import socket
import time


# define socket address
IP = '127.0.0.1'  # ip of the server we want to connect to
PORT = 10000  # port used for communicating with the server

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully.")

#bind server
s.bind((IP, PORT))
s.listen(5) #now wait for client connection

while True:
    try:
        c , addr = s.accept() #establish connection with the client
        print('Connection from %s',addr)
        msg = 'Thanks you for connecting!!'
        print(msg)
        c.send(msg.encode("utf-8"))
        time.sleep(3) ## sleep for 3 seconds until close the connection

        c.close()
    except (KeyboardInterrupt , SystemExit):
        print("interrup server")
        raise

s.close()
