__author__ = 'wanghao'

import threading
import sys
import socket
import os
import time

def run_flow(dst_ip, port, size):

    def run(dst_ip, port, size):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        data = os.urandom(size)
        #data = "1234567890"*size
        try:
            sock.connect((dst_ip, port))
            sock.sendall(data)
        except socket.timeout:
            print "Connection Timeout!"
        finally:
            sock.close()

    t = threading.Thread(target=run(dst_ip, port, size))
    t.start()


def main():

    dst_ip = sys.argv[1]
    port = int(sys.argv[2])
    size = int(sys.argv[3])

    print "Flow Size:", size
    start_t = time.time()
    print "Start:", time.strftime("%M:%S")
    run_flow(dst_ip, port, size)
    end_t = time.time()
    print "End:", time.strftime("%M:%S")

    print "Duration:", end_t - start_t

if __name__ == '__main__':
    main()