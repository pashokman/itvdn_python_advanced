import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 255.255.255.255 - send message to every client
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
# change value of param SO_BROADCAST to 1
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# change value of param SO_REUSEADDR to 1
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client, addr = sock.accept()
result = client.recv(1024)
client.close()

print('Message', result.decode('utf-8'))