import socket
import ssl


def connect_server(address, port):
    # tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    #                                  ca_certs="cert.pem", cert_reqs=ssl.CERT_REQUIRED
    # certificate = ssl.get_server_certificate((address, port))
    # print(certificate)
    # context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    # context.set_ciphers('DEFAULT@SECLEVEL=2')
    server_address = (address, port)

    context = ssl.create_default_context()
    tcp_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),
                                     server_hostname=server_address[0])
    # tcp_socket = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    tcp_socket.settimeout(500)

    server_addr = (address, port)
    tcp_socket.connect(server_addr)

    return tcp_socket


"User-Agent:Mozilla/5.0(Macintosh;Intel Mac 0sX10.15;rv:123.0)Gecko/2010010"
"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/we"
"Accept-Language:en-US,en;g=0.5Accept-Encoding:gzip，deflate，br"
"Referer: https://www.google.com/"
"Connection:keep-alive"
"Cookie: bid=quF_BCePijI; ap_v=0,6.0;__yadk_uid=TjpLQt5H6hkn6GvbRwvPFlQeDoHfewFQ"
"Upgrade-Insecure-Requests:1"
"Sec-Fetch-Dest:document"
"Sec-Fetch-Mode:navigate"
"Sec-Fetch-Site:cross-site"


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


# # 3. 发送数据
# send_data = input("请输入要发送的数据：")
# tcp_socket.send(send_data.encode("gbk"))
#
# # 4. 关闭套接字
# tcp_socket.close()

def main():
    https = connect_server("www.zhihu.com", 80)  # 这里的端口怎么获取

    send_data = data_content()

    print(send_data)

    https.send(send_data.encode())

    receive_data = https.recv(4096)

    receive_text = receive_data.decode()

    print(receive_text)


if __name__ == '__main__':
    main()
