#  Developed by Kostas.Makedos
#  kostas.makedos@gmail.com: 4/14/19, 9:52 PM
#  Last Modified 4/14/19, 9:42 PM
#  Copyright (c) 2019
#  All rights reserved.

import socket
class Observer:
    def __init__(self):
        print("Observer started")
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        ipv4, ipv5 = socket.getaddrinfo(None, 9000, 0, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
        host = ipv4[-1][0]
        port = 9000
        self._socket.bind((host, port))
        self._socket.listen(1)
        print("Listening to %s:%s" % (host, port))

        while True:
            c,addr = self._socket.accept()
            print("Got connection from ",  addr)
            while True:
                mesg = self._recv_all(c, 1024)
                if mesg:
                    print(mesg)
                else:
                    break


ob = Observer()



