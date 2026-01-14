# server side socket
import socket

server_socket = socket.socket()
server_socket.bind(('localhost', 3000))

server_socket.listen(1)
print("Server is listening on port 3000...")

conn, addr = server_socket.accept()
print(f"Connected with {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Client: {data}")
    conn.send(f"Received: {data}".encode())
    
conn.close() 