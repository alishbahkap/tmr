import socket

recIP = "127.0.0.1"
port = 5555
buff = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((recIP, port))

print("Listening...")

while True:
    data, sender = sock.recvfrom(buff)
    print("Received:", data.decode())
