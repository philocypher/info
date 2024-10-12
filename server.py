import socket

address = ("127.0.0.1","80")
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

while True:
    #conn, client_address = server.accept()
