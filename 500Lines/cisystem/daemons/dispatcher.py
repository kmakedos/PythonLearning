#  Developed by Kostas.Makedos
#  kostas.makedos@gmail.com: 4/14/19, 9:52 PM
#  Last Modified 4/14/19, 7:32 PM
#  Copyright (c) 2019
#  All rights reserved.


import queue
import socketserver
from networks import netutils
from models import job

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        msg = self.request.recv(1024).strip()
        current_job = job.Job()
        current_job.unserialize(msg)
        self.server.server_data = current_job.data



class Dispatcher:
    def __init__(self, config_path="config/config.ini"):
        self.server = netutils.Server(config_path, target='dispatcher', handler=Handler)
        self._queue = queue.Queue()

    def put(self, item):
        self._queue.put(item)

    def start(self):
        self.server.start()
        #while not self._queue.empty():
        #    self._send_message(self._queue.get())
