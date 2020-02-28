import socket
import threading
from _thread import *


print_lock = threading.Lock()


def client_thread(connection, hostaddr, port):
    while True:
        print('Connected with ', hostaddr, ':', port)
        received_data = connection.recv(1028)
        decoded_data = received_data.decode("utf8").rstrip()  # decode and strip end of line
        print(decoded_data)
    connection.close()


if __name__ == '__main__':
    # create an AF_INET, STREAM socket (TCP)
    sserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sserver.bind(('localhost', 12345))
    print('Socket now listening')
    sserver.listen(5)
    while True:
        connection, (hostaddr, port) = sserver.accept()
        print_lock.acquire()
        start_new_thread(client_thread, (connection, hostaddr, port))

    sserver.close()

