# coding:gbk
import socket

# 创建一个 TCP/IP 套接字
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定套接字到端口
server_address = ('localhost',8888)
print('启动服务器 {} 端口{}'.format(*server_address))
server_socket.bind(server_address)

# 监听连接
server_socket.listen(1)

while True:
    # 等待连接
    print('等待连接....')
    connection,client_address = server_socket.accept()

    try:
        print('连接来自：',client_address)

        # 接收数据
        while True:
            data = connection.recv(1024)
            data_text = data.decode('utf-8')
            print('接收到',data_text)
            if data:
                print('发送回数据')
                connection.sendall(data)
            else:
                print('没有数据,关闭连接')
                break
    finally:
        # 清理连接
        connection.close()