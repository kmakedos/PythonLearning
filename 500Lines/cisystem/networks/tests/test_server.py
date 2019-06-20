from unittest import TestCase
import socket
from networks import utilities



class TestConnections(TestCase):
    def setUp(self):
        self.server = utilities.Server()
        client = utilities.Client()

    def test_run(self):
        self.server.start()



    def test_stop(self):
        pass

    def tearDown(self):
        self.Server = None
