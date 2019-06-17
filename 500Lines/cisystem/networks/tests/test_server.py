from unittest import TestCase
import socket
from networks import utilities
import multiprocessing



class TestConnections(TestCase):
    def setUp(self):
        pass

    def test_run(self):
        self.serverProcess = multiprocessing.Process(name = utilities.Server.run)
        self.clientProcess = multiprocessing.Process(name = utilities.Client)
        self.serverProcess.start()
        self.clientProcess.start()
        self.serverProcess.join()
        self.clientProcess.join()



    def test_stop(self):
        pass

    def tearDown(self):
        self.Server = None
