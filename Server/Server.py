# coding:gbk
import socket

# ����һ�� TCP/IP �׽���
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# ���׽��ֵ��˿�
server_address = ('localhost',8888)
print('���������� {} �˿�{}'.format(*server_address))
server_socket.bind(server_address)

# ��������
server_socket.listen(1)

while True:
    # �ȴ�����
    print('�ȴ�����....')
    connection,client_address = server_socket.accept()

    try:
        print('�������ԣ�',client_address)

        # ��������
        while True:
            data = connection.recv(1024)
            data_text = data.decode('utf-8')
            print('���յ�',data_text)
            if data:
                print('���ͻ�����')
                connection.sendall(data)
            else:
                print('û������,�ر�����')
                break
    finally:
        # ��������
        connection.close()