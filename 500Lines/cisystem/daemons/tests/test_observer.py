from unittest import TestCase
from networks import netutils
from daemons import observer


class TestObserver(TestCase):
    def setup_class(self):
        self.server = netutils.Server(config_path="daemons/tests/config.ini")
        self.observer = observer.Observer(config_path="daemons/tests/config.ini")

    def test_observer(self):
        self.server.start()
        self.observer.start()

    def teardown_class(self):
        self.observer = None
