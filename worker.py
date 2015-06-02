__author__ = 'wanghao'

import subprocess
import threading
import SocketServer
import socket
import Pyro4
import sys
import os

class TCPHander(SocketServer.StreamRequestHandler):
    def handle(self):
        recv_data = ""
        while 1:
            data = self.request.recv(1024)
            if not data:
                break
            recv_data += data

        print len(recv_data)

class Worker(object):
    def __init__(self, name):
        self.worker_name = name

    def socket_listen(self):
        # start a socket server, listening to 10087
        server = SocketServer.TCPServer((self.worker_name, 10087), TCPHander)
        print "Worker socket server starts at 10087"
        t = threading.Thread(target=server.serve_forever)
        t.start()

    def run_flow(self, dst_ip, port, size):

        def run(dst_ip, port, size):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            data = os.urandom(size)
            try:
                sock.connect((dst_ip, port))
                sock.sendall(data)
            finally:
                sock.close()

        t = threading.Thread(target=run(dst_ip, port, size))
        t.start()

    def who(self):
        who = "I am alive @ %s." % self.worker_name
        print who
        return who

def main():
    worker_name = sys.argv[1]
    worker = Worker(worker_name)
    worker.socket_listen()

    daemon = Pyro4.Daemon(host=worker_name, port=10086)
    uri = daemon.register(worker, worker_name)

    print "Worker starts at %s" % uri

    daemon.requestLoop()                   # start the event loop of the server to wait for calls

if __name__ == '__main__':
    main()
