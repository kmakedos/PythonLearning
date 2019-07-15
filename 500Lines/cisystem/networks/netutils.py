#  Developed by Kostas.Makedos
#  kostas.makedos@gmail.com: 4/14/19, 9:52 PM
#  Last Modified 4/14/19, 9:52 PM
#  Copyright (c) 2019
#  All rights reserved.

import socketserver
import socket
import threading
import configparser
from networks import request_handler

class ThreadingSocketServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Server():

    def __init__(self, config_path='config.ini', target='default', handler=request_handler.RequestHandler):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        host = self.config[target]['Host']
        port = int(self.config[target]['Port'])
        self.server = ThreadingSocketServer((host, port), handler)
        self.server_data = None

    def start(self):
        self.server_thread = threading.Thread(target = self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.allow_reuse_address = True
        self.server_thread.start()


class Client:
    def __init__(self, config_path="config/config.ini", target='default'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self._host = self.config[target]['Host']
        self._port = int(self.config[target]['Port'])
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_message(self, message="Hello"):
        if message is not None:
            self._socket.connect(((self._host, self._port)))
            self._socket.send(message.encode())
        else:
            print("Error: Empty message received!")
        self._socket.close()
