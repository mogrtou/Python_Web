import socket
import ssl

class Request_Socket(object):
    tcp_socket = None
    def __init__(self, address, pot, method, request_line, request_header, request_user):
        self.address = address
        self.pot = pot
        self.method = method
        self.request_line = request_line
        self.request_header = request_header
        self.request_user = request_user


    def connect_server(self):

        server_addr = (self.address, self.pot)
        context = ssl.create_default_context()
        self.tcp_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),
                                         server_hostname=server_addr[0])
        self.tcp_socket.connect(server_addr)

        # request_line = self.request_line + "\r\n"
        # request_header = self.request_header + "\r\n"
        # request_user = self.request_user + "\r\n"
        #
        # # request_date = request_line + request_header + request_user
        # #
        # # self.tcp_socket.send(request_date.encode())
        # #
        # # receive_data = self.tcp_socket.recv(4096)
        # #
        # # receive_text = receive_data.decode()
        # #
        # # print(receive_text)

    def request_data(self):

        request_line = self.request_line + "\r\n"
        request_header = self.request_header + "\r\n"
        request_user = self.request_user + "\r\n"

        request_date = request_line + request_header + request_user + "\r\n"

        self.tcp_socket.send(request_date.encode())

        receive_data = self.tcp_socket.recv(4096)

        receive_text = receive_data.decode()

        print(receive_text)