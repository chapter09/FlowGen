__author__ = 'v-whao'

import time
from SocketServer import *
from socket import error as SocketError
import sys

class TCPHandler(StreamRequestHandler):
    def handle(self):
        log_fd = open("./FlowGen.txt", "a")
        start_time = time.time()
        size = 0

        try:
            while 1:
                print "%f" % time.time()
                data = self.request.recv(12800)
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
        log_fd.write(log + "\n")


if __name__ == '__main__':
    port = int(sys.argv[1])
    try:
        # start a socket server, listening to 10087
        server = ForkingTCPServer(("0.0.0.0", port), TCPHandler)
        print "Socket server starts at %d" % port
        # socket_t = threading.Thread(target=server.serve_forever)
        server.serve_forever()
        # socket_t.start()
    except KeyboardInterrupt:
        exit(0)
