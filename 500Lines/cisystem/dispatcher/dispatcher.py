

#  Developed by Kostas.Makedos
#  kostas.makedos@gmail.com: 4/14/19, 9:52 PM
#  Last Modified 4/14/19, 7:32 PM
#  Copyright (c) 2019
#  All rights reserved.

import socket
import queue


class Dispatcher:
    def __init__(self, host, port):
        self._queue = queue.Queue()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((host, port))

    def _send_message(self, msg):
        self._socket.sendall(msg.encode())

    def put(self, item):
        self._queue.put(item)

    def run(self):
        while not self._queue.empty():
            self._send_message(self._queue.get())


df = Dispatcher("192.168.2.110", 9000)
for x in range(10):
    df.put(str(x))
df.run()
