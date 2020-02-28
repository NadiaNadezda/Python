import socket
from time import sleep

if __name__ == '__main__':
    sclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sclient.connect(('localhost', 12345))
    message = b'This is the message.'
    sclient.sendall(message)
    sleep(10)
    sclient.close()
