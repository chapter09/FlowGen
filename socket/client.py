__author__ = 'wanghao'

# import threading
import sys
import socket
from struct import *
import time
import threading

def run_flow(dst_ip, port, size):

    def run(dst_ip, port, size):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # data = os.urandom(size)
        data = pack('c', 'a')
        try:
            sock.connect((dst_ip, port))
            size_left = size
            while size_left:
                if size_left > 200000000:
                    sock.sendall(data*200000000)
                    size_left -= 200000000
                else:
                    sock.sendall(data*size_left)
                    size_left = 0

        except socket.timeout:
            print "Connection Timeout!"
        except socket.error, e:
            print e
        finally:
            sock.close()

    t = threading.Thread(target=run(dst_ip, port, size))
    t.start()
    t.join()
    print "Done"
    #run(dst_ip, port, size)


if __name__ == '__main__':
    dst_ip = sys.argv[1]
    port = int(sys.argv[2])
    size = int(float(sys.argv[3]))

    fd = open("fct.txt", 'a')

    print "Flow Size:", size
    fd.write("Flow Size %d " % size)

    start_t = time.time()
    #print "Start:", time.strftime("%M:%S")
    fd.write("Start: %s " % time.strftime("%M:%S"))

    run_flow(dst_ip, port, size)

    end_t = time.time()
    #print "End:", time.strftime("%M:%S")

    fd.write("End: %s " % time.strftime("%M:%S"))
    print "Duration:", end_t - start_t

    fd.write("Duration: %f \r\n" % (end_t - start_t))
    fd.close()