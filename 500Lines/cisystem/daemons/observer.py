#  Developed by Kostas.Makedos
#  kostas.makedos@gmail.com: 4/14/19, 9:52 PM
#  Last Modified 4/14/19, 9:42 PM
#  Copyright (c) 2019
#  All rights reserved.
from networks import netutils

class Observer:
    def __init__(self, config_path="config.ini"):
        self.client = netutils.Client(config_path)

    def start(self):
        self.client.send_message("Observer started")


