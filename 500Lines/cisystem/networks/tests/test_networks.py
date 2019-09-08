from unittest import TestCase
from networks import networks
import asyncio


class TestServer(TestCase):
    async def handle_connection(self, reader, writer):
        line = await reader.readline()
        print(line)

    def setup_class(self):
        self.loop = asyncio.get_event_loop()
        self.server = networks.Server(io_service=self.loop, handler=self.handle_connection, config_path="config.ini")
        self.server.start()

    def test_send_default(self):
        client = networks.Client(config_path="config.ini")
        self.loop.run_until_complete(client.send_message("First message from client"))

        

    def test_send_null_message(self):
        client = networks.Client(config_path="config.ini")
        self.loop.run_until_complete(client.send_message(None))

#    def test_send_custom_message(self):
#        self.client = netutils.Client(config_path="networks/tests/config.ini")
#        self.client.send_message("Custom message send from space!")
#
#    def test_send_to_custom_server(self):
#        self.client = netutils.Client(config_path="networks/tests/config2.ini")
#        self.client.send_message("A port to 20000 leagues")

    def teardown_class(self):
        self.client = None
        self.loop.call_later(5, self.loop.stop)
        self.loop.close()

