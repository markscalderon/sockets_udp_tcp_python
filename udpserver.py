import socket
IP = "127.0.0.1"
PORT = 6790
BUFFER_SIZE = 1024
#declare the server as UDP server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind the server with the socket
sock.bind((IP,PORT))

while True:
    try:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        print("Message")
        print( data)
        pass
    except  (KeyboardInterrupt , SystemExit):
        raise

sock.close()
