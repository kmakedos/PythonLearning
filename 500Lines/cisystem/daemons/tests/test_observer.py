from unittest import TestCase
from networks import utilities
from daemons import observer


class TestObserver(TestCase):
    def setup_class(self):
        self.server = utilities.Server()
        self.observer = observer.Observer()

    def test_observer(self):
        self.server.start()
        self.observer.start()

    def teardown_class(self):
        self.observer = None
