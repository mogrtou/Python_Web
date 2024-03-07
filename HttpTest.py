import socket
import ssl


def connect_server(address, port):

    server_addr = (address, port)
    context = ssl.create_default_context()
    tcp_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),
                                     server_hostname=server_addr[0])
    tcp_socket.connect(server_addr)

    return tcp_socket



def data_content():
    request_line = "GET /top250 HTTP/1.1\r\n"

    request_Header = "Host: movie.douban.com\r\n"

    request_User = "User-Agent:Mozilla/5.0(Macintosh;Intel Mac 0sX10.15;rv:123.0)Gecko/2010010\r\n"

    request_Accept = "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/we\r\n"

    request_Language = "Accept-Language:en-US,en;g=0.5Accept-Encoding:gzip，deflate，br\r\n"

    request_Referer = "Referer: https://www.google.com/\r\n"

    request_Connection = "Connection:keep-alive\r\n"

    request_Cookie = "Cookie: bid=quF_BCePijI; ap_v=0,6.0;__yadk_uid=TjpLQt5H6hkn6GvbRwvPFlQeDoHfewFQ\r\n"

    request_Upgrade = "Upgrade-Insecure-Requests:1\r\n"

    request_Dest = "Sec-Fetch-Dest:document\r\n"

    request_Mode = "Sec-Fetch-Mode:navigate\r\n"

    request_Site = "Sec-Fetch-Site:cross-site\r\n"

    # request_User = "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0\r\n"

    request_blank = "\r\n"

    request_data = (request_line + request_Header + request_User + request_Accept + request_Language + request_Referer
                    + request_Connection + request_Cookie + request_Upgrade + request_Dest
                    + request_Mode + request_Site + request_blank)

    return request_data


def main():
    https = connect_server("movie.douban.com", 443)  # 这里的端口怎么获取

    send_data = data_content()

    https.send(send_data.encode())

    receive_data = https.recv(4096)

    receive_text = receive_data.decode()

    print(receive_text)


if __name__ == '__main__':
    main()
