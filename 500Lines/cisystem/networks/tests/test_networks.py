import socket
from unittest import TestCase
from networks import utilities


class TestServer(TestCase):
    def setup_class(self):
        self.default_server = utilities.Server()
        self.default_server.start()
        self.custom_server = utilities.Server(host="127.0.0.1", port=20000)

    def test_send_default(self):
        self.client = utilities.Client()
        self.client.send_message()

    def test_send_null_message(self):
        self.client = utilities.Client()
        self.client.send_message(message=None)

    def test_send_custom_message(self):
        self.client = utilities.Client()
        self.client.send_message("Custom message send from space!")

    def test_send_to_custom_server(self):
        self.client = utilities.Client(host="127.0.0.1", port=20000)
        self.client.send_message("A port to 20000 leagues")

    def teardown_class(self):
        self.client = None
