__author__ = 'wanghao'

import os
import threading
import socket
import Pyro4

class Controller(object):
    def __init__(self):
        # client URI format is PYRO:IP@hostname:port
        # e.g.: PYRO:202.120.1.101@localhost:10086

        self.clients = ["PYRO:202.120.1.101@localhost:10086"]
        self.conf = {}

    def read_conf(self):
        pass

    def register(self):
        pass

    def collect(self):
        pass


def main():
    controller = Controller()

    for client in controller.clients:
        worker = Pyro4.core.Proxy(client)
        print(worker.who())
        worker.run_flow("localhost", 10087, 502400)



if __name__ == '__main__':
    print "Controller starts..."
    main()
