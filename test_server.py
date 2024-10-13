import unittest
import socket
import threading
import time
from server import echo_server

class TestEchoServer(unittest.TestCase):

    def test_echo(self):
        server_thread = threading.Thread(target=echo_server)
        server_thread.start()
        time.sleep(1)  # Give the server time to start

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(('localhost', 12345))
            message = b'Hello, server!'
            sock.sendall(message)
            data = sock.recv(1024)
            self.assertEqual(data, message)

        server_thread.join(timeout=1)  # Attempt to stop the server


if __name__ == '__main__':
    unittest.main()
