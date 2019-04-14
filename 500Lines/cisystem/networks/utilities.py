
#  Developed by Kostas.Makedos
#  kostas.makedos@gmail.com: 4/14/19, 9:52 PM
#  Last Modified 4/14/19, 9:52 PM
#  Copyright (c) 2019
#  All rights reserved.

import socket


class Server:

    def __init__(self, hostIP="0.0.0.0", port=9000):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self._hostIP = hostIP
        self._port = port

    def run(self):
        self._socket.bind((self._hostIP, self._port))
        self._socket.listen(1)
        while True:
            c,addr = self._socket.accept()
            print("Got connection from ",  addr)
            while True:
                mesg = self._recv_all(c, 1024)
                if mesg:
                    print(mesg)
                    exit()
                else:
                    break


    def _recv_all(self, client_socket, length):
        data = ''
        while len(data) < length:
            more = client_socket.recv(length - len(data))
            if not more:
                return data
            data += more.decode()
        return data



    def stop(self):
        self._socket.shutdown(socket.SHUT_RDWR)
        self._socket.close()



class Client:
    def __init__(self, hostIP="0.0.0.0", port=9000):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._hostIP = hostIP
        self._port = port

    def send_message(self, message):
        self._socket.connect(((self._hostIP, self._port)))
        self._socket.send(message.encode())



