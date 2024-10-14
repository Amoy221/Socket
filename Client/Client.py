# coding:gbk
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ���ӷ�����
server_address = ('localhost', 8888)
print('���ӵ������� {} �˿� {}'.format(*server_address))
client_socket.connect(server_address)

try:
    # ��������
    message = input('��������Ҫ���͵����ݣ�')
    message = message.encode('utf-8') # ���ַ���ת���ɶ���������
    print('����: {!r}'.format(message))
    client_socket.sendall(message)

    # ������Ӧ
    data = client_socket.recv(1024)
    data = data.decode('utf-8') # �Ѷ���������ת�����ַ���
    print('����: {!r}'.format(data))

finally:
    # �ر�����
    print('�ر�����')
    client_socket.close()