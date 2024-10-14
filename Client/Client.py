# coding:gbk
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
server_address = ('localhost', 8888)
print('连接到服务器 {} 端口 {}'.format(*server_address))
client_socket.connect(server_address)

try:
    # 发送数据
    message = input('请输入你要发送的数据：')
    message = message.encode('utf-8') # 把字符串转换成二进制数据
    print('发送: {!r}'.format(message))
    client_socket.sendall(message)

    # 接收响应
    data = client_socket.recv(1024)
    data = data.decode('utf-8') # 把二进制数据转换成字符串
    print('接收: {!r}'.format(data))

finally:
    # 关闭连接
    print('关闭连接')
    client_socket.close()