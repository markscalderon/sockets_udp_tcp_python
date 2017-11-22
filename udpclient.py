import socket
IP = "127.0.0.1"
PORT = 6790
BUFFER_SIZE = 1024
#declare the server as UDP server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Hello server!"
sock.sendto(msg.encode("utf-8"), (IP, PORT))
sock.close()
