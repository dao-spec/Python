import socket
import threading
import time


def tplink(sock, addr):
    print('S ->> Accept new connection from %s: %s...' % addr)
    sock.send(b'Wellcom!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('YES: %s !' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('S ->> Connection from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 2048))
s.listen(4)
print('S -> Waiting for connection')

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tplink, args=(sock, addr))
    t.start()

