import socket

# create instance of class socket with 2 constants - AF_INET (use IP protocol of ver.4), SOCK_STREAM (use protocol TCP)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# add ip address and port to our new socket instance (if ip = '' or '0', it means reserv all interfaces - all ip's)
sock.bind(('127.0.0.1', 8888))

# how much connections we will be listening
sock.listen(5)

while(True):
    try:
        # look into the queue is there are some connections (if queue is empty, wait for the first connection), return client socket and address
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        # recv - method recieve 1024 bytes (buffer size)
        result = client.recv(1024)
        client.close()
        print('Message', result.decode('utf-8'))