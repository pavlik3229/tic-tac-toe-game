import socket

HOST = (socket.gethostname(), 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
print("Connected to", HOST)

while True:
    message = client.recv(1024).decode("UTF-8")
    if len(message) != 0:
        print(message)
        continue