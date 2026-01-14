# client side socket
import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 3000))

while True:
    msg = input("Enter message to send (You): ")
    client_socket.send(msg.encode())
    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")

