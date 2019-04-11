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

df = Dispatcher("Lubi", 9000)
for x in range(10):
    df.put(str(x))
df.run()
