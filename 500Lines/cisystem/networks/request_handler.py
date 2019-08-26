import socketserver
class RequestHandler(socketserver.BaseRequestHandler):
    """
    The request handler must be instantiated once per connection and must
    override the handle() method to implement communication to the client
    """
    def __init__(self, callback=None, *args, **kwargs):
        self.callback = callback
        socketserver.BaseRequestHandler.__init__(self, *args, **kwargs)
        self.data = None

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.callback(self.data)

    @staticmethod
    def handle_factory(callback):
        def createHandler(*args, **kwargs):
            return RequestHandler(callback, *args, **kwargs)
<<<<<<< HEAD
        return create_handler
=======
        return createHandler

>>>>>>> 4c68415b22a398b9caf451efd0c51d2c5b06c25d

