
#  Developed by Kostas.Makedos
#  kostas.makedos@gmail.com: 4/14/19, 9:52 PM
#  Last Modified 4/14/19, 9:52 PM
#  Copyright (c) 2019
#  All rights reserved.

import socketserver
import socket


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


class Server():

    def __init__(self, host="0.0.0.0", port=9000):
        self.server = socketserver.TCPServer((host, port), RequestHandler)
        self.server.allow_reuse_address = True

    def run(self):
        with self.server:
            self.server.serve_forever()

class Client:
    def __init__(self, hostIP="0.0.0.0", port=9000):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._hostIP = hostIP
        self._port = port
        
    def send_message(self, message):
        self._socket.connect(((self._hostIP, self._port)))
        self._socket.send(message.encode())
