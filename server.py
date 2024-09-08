import socket
import time

HOST = (socket.gethostname(), 10000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(HOST)
server.listen()
print("Listening to connections 👀")

client_socket, addr = server.accept()
print("Connected -", addr)
while True:

    res = bytes(input(), "UTF-8")
    client_socket.send(res)
    continue

client_socket.close()
print("connection closed")