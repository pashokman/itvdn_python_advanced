# recieve only one message
import socket

# create instance of class socket with 2 constants - AF_INET (use IP protocol of ver.4), SOCK_DGRAM (use protocol UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# add ip address and port to our new socket instance (if ip = '' or '0', it means reserv all interfaces - all ip's)
sock.bind(('127.0.0.1', 8888))

# recv - method recieve 1024 bytes (buffer size)
result = sock.recv(1024)

# waiting until client send a message to the socket and then pring message and close the socket
print('Message', result.decode('utf-8'))
sock.close()