

from socketserver import BaseRequestHandler, TCPServer

class Handler(BaseRequestHandler):
    def handle(self):
        print('get connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


if __name__ == "__main__":
    serv = TCPServer(('', 7777), Handler)
    serv.serve_forever()