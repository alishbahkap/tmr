import socket

targIP = "127.0.0.1"
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(
    "Hello from sender".encode(),
    (targIP, port)
)

print("Message sent")
# 