

import socket
import sys


server = (input("enter sevrer address-> "),12345)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(server)
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")
