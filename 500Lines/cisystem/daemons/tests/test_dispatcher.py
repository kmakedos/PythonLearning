from unittest import TestCase
from networks import utilities
from daemons import dispatcher


class TestDispatcher(TestCase):
    def setup_class(self):
        self.dispatcher = dispatcher.Dispatcher()
        self.client = utilities.Client()

    def test_dispatcher(self):
        self.dispatcher.start()
        self.client.send_message("A message for dispatcher")

    def teardown_class(self):
        self.dispatcher = None
