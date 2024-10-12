import socket

address = ("127.0.0.1","80")
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
  server.bind(address)
  server.listen(5)

# while True:
#     conn, client_address = server.accept()
#     with conn:
#         conn
