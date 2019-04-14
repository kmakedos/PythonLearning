

#  Developed by Kostas Makedos
#  kostas.makedos@gmail.com : 14/4/2019 7:17 μμ
#  Last Modified 14/4/2019 7:13 μμ
#  Copyright (c) 2019.
#  All rights reserved.

import socket


class Observer:
    def __init__(self):
        print("Observer started")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        host = socket.gethostname()
        port = 9000
        s.bind((host, port))
        s.listen(5)
        print("Listening to %s:%s" % (host, port))

        while True:
            c, addr = s.accept()
            print("Got connection from ", addr)
            mesg = c.recv(16)
            print(mesg.decode())

        c.close()


ob = Observer()
