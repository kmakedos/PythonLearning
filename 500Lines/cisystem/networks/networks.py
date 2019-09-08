import asyncio
import configparser


class Server():
    def __init__(self, io_service, handler, config_path='config.ini', config_section='default'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self._host = self.config[config_section]['Host']
        self._port = self.config[config_section]['Port']
        self._io_service = io_service
        self._handler = handler
        self._server = None

    def start(self):
        self._server = asyncio.start_server(self._handler, self._host, self._port)
        self._io_service.run_until_complete(self._server)


class Client():

    def __init__(self, config_path='config.ini', config_section='default'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self._host = self.config[config_section]['Host']
        self._port = self.config[config_section]['Port']

    async def send_message(self, message):
        reader, writer = await asyncio.open_connection(self._host, self._port)
        writer.write(message.encode())
        await writer.drain()
        writer.close()






