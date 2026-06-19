import socket
import json

recIP = "127.0.0.1"
port = 5555
buff  = 65535

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((recIP, port))

print("Listening...")

while True:
    data, sender = sock.recvfrom(buff)
    num = json.loads(data.decode())
    print("Received:", num)
