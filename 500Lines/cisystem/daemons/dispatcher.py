#  Developed by Kostas.Makedos
#  kostas.makedos@gmail.com: 4/14/19, 9:52 PM
#  Last Modified 4/14/19, 7:32 PM
#  Copyright (c) 2019
#  All rights reserved.

from networks import netutils
import queue


class Dispatcher:
    def __init__(self, config_path="config.ini"):
        self._queue = queue.Queue()
        self.server = netutils.Server(config_path)

    def put(self, item):
        self._queue.put(item)

    def start(self):
        self.server.start()
        #while not self._queue.empty():
        #    self._send_message(self._queue.get())
