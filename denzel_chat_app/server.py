# server.py

import socket

HOST = 'localhost'
PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []

print("Server listening on {}, port {}".format(HOST, PORT))

while True:
    client_socket, address = server_socket.accept()
    print("New connection from {}".format(address))
    clients.append(client_socket)

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        for client in clients:
            if client != client_socket:
                client.send(data)

    print("Connection from {} closed".format(address))
