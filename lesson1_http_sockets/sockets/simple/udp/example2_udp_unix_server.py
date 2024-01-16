#  Use file instead of socket on this local machine
import os
import socket

# create file socket name
unix_sock_name = 'unix.sock'
# create an instance of socket object with protocol AF_UNIX instead of AF_INET
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

sock.bind(unix_sock_name)

while(True):
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message', result.decode('utf-8'))