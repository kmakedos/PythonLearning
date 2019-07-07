#  Developed by Kostas.Makedos
#  kostas.makedos@gmail.com: 4/14/19, 9:52 PM
#  Last Modified 4/14/19, 7:32 PM
#  Copyright (c) 2019
#  All rights reserved.


import queue
import socketserver
from networks import netutils

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("Dispatcher received : ", self.data)
        # Here the message which should be a job description
        # should be put in the queue and an appropriate worker should pick it

class Dispatcher:
    def __init__(self, config_path="config.ini"):
        self._queue = queue.Queue()
        self.server = netutils.Server(config_path, Handler)

    def put(self, item):
        self._queue.put(item)

    def start(self):
        self.server.start()
        #while not self._queue.empty():
        #    self._send_message(self._queue.get())
