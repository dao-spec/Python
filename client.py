import socket
import threading
import time
def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 2048))
    print(s.recv(1024).decode('utf-8'))

    for data in [b'Dao', b'Tracy', b'Sarah']:
        s.send(data)
        print('%s - %s' % (threading.current_thread().name,s.recv(1024).decode('utf-8')))
        time.sleep(1)

    s.send(b'exit')
    s.close()


if __name__ == "__main__":
    for x in range(1,800):
        threadName = 'thread-' + str(x)
        thread = threading.Thread(target=client, name=threadName)
        thread.start()