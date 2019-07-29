#  Developed by Kostas.Makedos
#  kostas.makedos@gmail.com: 4/14/19, 9:52 PM
#  Last Modified 4/14/19, 7:32 PM
#  Copyright (c) 2019
#  All rights reserved.

import queue
from networks import netutils, request_handler
from models import job


class Dispatcher:
    def __init__(self, config_path="config/config.ini"):
        self.request_handler_factory = request_handler.RequestHandlerFactory()
        self.server = netutils.Server(config_path, target='dispatcher',
                                      handler=self.request_handler_factory.handle_factory(callback=self.put))
        print("Calling netutils Server with handler=", self.request_handler_factory.handle_factory(callback=self.put))
        self._queue = queue.Queue()

    def put(self, item):
        current_job = job.Job()
        current_job.unserialize(item)
        self._queue.put(current_job)

    def start(self):
        self.server.start()
        #while not self._queue.empty():
        #    self._send_message(self._queue.get())
