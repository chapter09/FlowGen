__author__ = 'v-whao'


import asyncore
import socket
import time
import sys
from socket import error as SocketError


class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        size = 0
        start_time = time.time()

        try:
            while 1:
                print "%f" % time.time()
                data = self.recv(12800)
                if not data:
                    break
                size += len(data)
        except MemoryError:
            print "Memory Error"
        except SocketError as e:
            print e

        end_time = time.time()
        log = "From: %s Size: %d Start: %f End: %f Duration: %f" % \
              (self.client_address, size, start_time, end_time, end_time - start_time)
        print log


class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = EchoHandler(sock)


if __name__ == "__main__":

    server = EchoServer('0.0.0.0', int(sys.argv[0]))
    asyncore.loop()