
#wsgi

import socket
import StringIO
import sys

class WSGIServer(object):

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address)
        #创建一个监听socket
        self.listen_socket = listen_socket =  socket.socket(
                self.address_family,
                self.socket_type
        )
        
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(server_address)
        listen_socket.listen(self.request_queue_size)
        #获取服务器地址和端口
        host, port = self.listen_socket.getsockname()[:2]

        self.sever_name = socket.getfqdn(host)
        self.sever_port = port
        self.headers_set = []
        
    def set_app(self, application):
        self.application = application

    def serve_forever(self):
        listen_socket = self.listen_socket

        while True:
            self.client_connection, client_address = listen_socket.accept()

            self.handle_one_request()





















