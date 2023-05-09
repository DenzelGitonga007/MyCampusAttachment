# client.py

import socket
import threading

HOST = 'localhost'
PORT = 9000

username = input('Enter your username: ')
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        data = client_socket.recv(1024).decode()
        print(data)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input()
    message = f'{username}: {message}'
    client_socket.send(message.encode())
