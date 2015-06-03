__author__ = 'v-whao'

import sys
from SocketServer import *

class TCPHander(StreamRequestHandler):
    def handle(self):
        print "start"
        # recv_data = ""
        try:
            while 1:
                data = self.request.recv(1024000)
                if not data:
                    break
                # recv_data += data

        except MemoryError:
            print "Memory Error"
        # print len(recv_data)
        print "end"


class TCPThreadingServer(ThreadingMixIn, TCPServer):
    pass


if __name__ == '__main__':
    port = int(sys.argv[1])
    try:
        # start a socket server, listening to 10087
        server = TCPThreadingServer(("0.0.0.0", port), TCPHander)
        print "Socket server starts at %d" % port
        # socket_t = threading.Thread(target=server.serve_forever)
        server.serve_forever()
        # socket_t.start()
    except KeyboardInterrupt:
        exit(0)
