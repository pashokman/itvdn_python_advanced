import socket

# __enter__/__exit__
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    print('8888 is bind')
    sock.bing(('127.0.0.1', 8888))

    while True:
        result = sock.recv(1024)
        print('Message', result.decode('utf-8'))