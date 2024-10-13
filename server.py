import socket
import threading

def handle_client(conn,client_address):
  print(f"Connection from {client_address}")
  try:
    while True:
        data = conn.recv(1024)
        if data:
          print(f"Received {data!r} from {client_address}")
          conn.sendall(data)
        else:
          print(f"No data from {client_address}")
          break
  finally:
      print(f"Closing connection from {client_address}")
      conn.close()




def echo_server():
  print("Starting echo server...")
  address = ("localhost",12345)
  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind(address)
    server.listen(5)
    while True:
      conn, client_address = server.accept()
      threading.Thread(target=lambda:handle_client(conn,client_address)).start()
if __name__ =="__main__":
    echo_server()
