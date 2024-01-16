import socket

# create instance of class socket with 2 constants - AF_INET (use IP protocol of ver.4), SOCK_DGRAM (use protocol UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send ,essage to the socket
sock.sendto(b'Test message', ('127.0.0.1', 8888))