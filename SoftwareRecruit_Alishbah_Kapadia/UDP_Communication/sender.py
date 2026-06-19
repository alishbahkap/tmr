import socket
import json 
import random

targIP = "127.0.0.1" 
port = 5555
num = [random.randint(0, 65535) for _ in range(100)] # assuming unsigned so 0 to 65535

message = json.dumps(num)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(
    message.encode(),
    (targIP, port)
)

print("Message sent")
# 