

#  Developed by Kostas Makedos
#  kostas.makedos@gmail.com : 14/4/2019 7:17 μμ
#  Last Modified 14/4/2019 7:13 μμ
#  Copyright (c) 2019.
#  All rights reserved.

import socket


class Server:

    def __init__(self, port=9000):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        ipv4, ipv6 = socket.getaddrinfo(None, port, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
        hostIP = ipv4[-1][0]
        self._socket.bind((hostIP, port))
        self._socket.listen(1)
