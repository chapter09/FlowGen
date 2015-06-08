__author__ = 'v-whao'

import sys
import subprocess
import time

DST = "10.11.9.3"
SRC_MAP = [
    "10.11.6.2",
    "10.11.6.3",
    "10.11.6.4",
    "10.11.7.2",
    "10.11.7.3",
    "10.11.7.4",
    "10.11.8.2",
    "10.11.8.3",
    "10.11.8.4",
    "10.11.9.2"
    ]


if __name__ == '__main__':
    conf = sys.argv[1]
    procs = []

    for i in (0, len(SRC_MAP)):
        p = subprocess.Popen(r'.\bin\nc.exe %s 10000' % SRC_MAP[i],
                             shell=True, stdin=subprocess.PIPE)
        procs.append(p)

    last_time = 0
    curr_time = 0
    fd = open(conf)

    while True:
        line = fd.readline()
        
        if not line:
            break
        
        rec = line.split(" ")

        src = SRC_MAP[int(rec[0])]
        last_time = curr_time
        curr_time = float(rec[2])
        size = rec[3].strip()

        print line

        client_proc = procs[int(rec[0])]
        time.sleep(curr_time - last_time)
        client_proc.stdin.write("python client.py %s 10087 %s\n" % (DST, size))
        # client_proc.stdin.write("python client.py 192.168.5.22 10087 42423.32\n")

    for proc in procs:
        proc.kill()









