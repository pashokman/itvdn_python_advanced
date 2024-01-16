import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
# if setblocking = True (by default while there is no client connection, wait for connection) 
# if setblocking = False (while there is no client connection, we get an exception) 
sock.setblocking(True)

client, addr = sock.accept()
result = client.recv(1024)
client.close()

print('Message', result.decode('utf-8'))