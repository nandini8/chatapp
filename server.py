import socket

host = '10.5.0.230'
port = 5000

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen()