#  Developed by Kostas.Makedos
#  kostas.makedos@gmail.com: 4/14/19, 9:52 PM
#  Last Modified 4/14/19, 9:52 PM
#  Copyright (c) 2019
#  All rights reserved.

import socketserver
import socket
import threading

class RequestHandler(socketserver.BaseRequestHandler):
    """
    The request handler must be instantiated once per connection and must
    override the handle() method to implement communication to the client
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

class ThreadingSocketServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Server():

    def __init__(self, host="0.0.0.0", port=9000):
        self.server = ThreadingSocketServer((host, port), RequestHandler)

    def start(self):
        self.server_thread = threading.Thread(target = self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.allow_reuse_address = True
        self.server_thread.start()
        print("Server running in thread: ", self.server_thread)


class Client:
    def __init__(self, host="0.0.0.0", port=9000):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._host = host
        self._port = port

    def send_message(self, message="Hello"):
        if message is not None:
            self._socket.connect(((self._host, self._port)))
            self._socket.send(message.encode())
        else:
            print("Error: Empty message received!")
        self._socket.close()
