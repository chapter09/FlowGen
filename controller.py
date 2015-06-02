__author__ = 'wanghao'

from multiprocessing import Process
import os
import Pyro4

class Controller(object):
    def __init__(self):
        self.clients = []
        self.conf = {}

    def read_conf(self):
        pass

    def register(self):
        pass

    def collect(self):
        pass


def main():
    controller = Controller()
    p = Process(target=Pyro4.naming.startNS)
    p.start()

    print "TEST"

    p.join() # this blocks until the process terminates


if __name__ == '__main__':
    print "Controller starts..."
    main()
