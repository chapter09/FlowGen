__author__ = 'v-whao'

import sys
import SocketServer

class TCPHander(SocketServer.StreamRequestHandler):
    def handle(self):
        recv_data = ""
        while 1:
            data = self.request.recv(1024)
            if not data:
                break
            recv_data += data

        print len(recv_data)

def main():

    port = int(sys.argv[1])
    try:
        # start a socket server, listening to 10087
        server = SocketServer.TCPServer(("localhost", port), TCPHander)
        print "Socket server starts at %d" % port
        # socket_t = threading.Thread(target=server.serve_forever)
        server.serve_forever()
        # socket_t.start()
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()
