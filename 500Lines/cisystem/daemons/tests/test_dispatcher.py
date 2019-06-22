from unittest import TestCase
from networks import netutils
from daemons import dispatcher


class TestDispatcher(TestCase):
    def setup_class(self):
        self.dispatcher = dispatcher.Dispatcher(config_path="daemons/tests/config.ini")
        self.client = netutils.Client(config_path="daemons/tests/config.ini")

    def test_dispatcher(self):
        self.dispatcher.start()
        self.client.send_message("A message for dispatcher")

    def teardown_class(self):
        self.dispatcher = None
