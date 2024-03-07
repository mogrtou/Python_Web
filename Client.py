import socket
# 1.创建socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname("https://movie.douban.com")
print(host)

# 2. 链接服务器
server_addr = ("192.168.1.4", 8080)
tcp_socket.connect(server_addr)

# 3. 发送数据
send_data = input("请输入要发送的数据：")
tcp_socket.send(send_data.encode("gbk"))

# 4. 关闭套接字
tcp_socket.close()