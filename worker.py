__author__ = 'wanghao'

import subprocess
import os
import Pyro4
import sys

class Worker(object):
    def __init__(self):
        pass

    def register(self):
        pass

    def socket_listen(self):
        pass

    def run_flow(self, dst, size):
        pass


def main():
    worker = Worker()

    daemon = Pyro4.Daemon()                # make a Pyro daemon
    ns = Pyro4.locateNS()                  # find the name server
    uri = daemon.register(worker)  # register the greeting object as a Pyro object
    ns.register("ipaddr", uri)   # register the object with a name in the name server
    print "Worker starts..."

    daemon.requestLoop()                   # start the event loop of the server to wait for calls

if __name__ == '__main__':
    main()
