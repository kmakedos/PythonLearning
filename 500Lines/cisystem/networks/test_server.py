from unittest import TestCase
import socket
import utilities
import multiprocessing



class TestConnections(TestCase):
    def setUp(self):
        self.Server = utilities.Server()
        self.Client = utilities.Client()

    def test_run(self):
        self.serverProcess = multiprocessing.Process(target = self.Server.run)
        self.clientProcess = multiprocessing.Process(target = self.Client.send_message, args=("123324",))
        self.serverProcess.start()
        self.clientProcess.start()
        self.serverProcess.join()
        self.clientProcess.join()


    def test_stop(self):
        pass

    def tearDown(self):
        self.Server = None
