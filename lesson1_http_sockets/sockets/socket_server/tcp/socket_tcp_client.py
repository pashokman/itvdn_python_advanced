import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))

sock.send(b'Test message')
result = sock.recv(64)
print('response', result.decode('utf-8'))
sock.close()