#  Developed by Kostas.Makedos
#  kostas.makedos@gmail.com: 4/14/19, 9:52 PM
#  Last Modified 4/14/19, 9:42 PM
#  Copyright (c) 2019
#  All rights reserved.
from networks import utilities

class Observer:
    def __init__(self):
        self.client = utilities.Client()

    def start(self):
        self.client.send_message("Observer started")
