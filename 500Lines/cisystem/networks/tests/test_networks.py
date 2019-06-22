import socket
from unittest import TestCase
from networks import netutils


class TestServer(TestCase):
    def setup_class(self):
        self.default_server = netutils.Server(config_path="networks/tests/config.ini")
        self.default_server.start()
        self.custom_server = netutils.Server(config_path="networks/tests/config2.ini")

    def test_send_default(self):
        self.client = netutils.Client(config_path="networks/tests/config.ini")
        self.client.send_message()

    def test_send_null_message(self):
        self.client = netutils.Client(config_path="networks/tests/config.ini")
        self.client.send_message(message=None)

    def test_send_custom_message(self):
        self.client = netutils.Client(config_path="networks/tests/config.ini")
        self.client.send_message("Custom message send from space!")

    def test_send_to_custom_server(self):
        self.client = netutils.Client(config_path="networks/tests/config2.ini")
        self.client.send_message("A port to 20000 leagues")

    def teardown_class(self):
        self.client = None
