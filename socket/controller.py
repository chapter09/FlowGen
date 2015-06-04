__author__ = 'v-whao'

import sys
import subprocess
import time

DST = "192.168.5.22"
SRC_MAP = [
    "192.168.5.19"
]


if __name__ == '__main__':
    conf = sys.argv[1]
    procs = []

    for i in (0, len(SRC_MAP)):
        p = subprocess.Popen(r'.\bin\nc.exe %s 10000' % "192.168.5.19",
                             shell=True, stdin=subprocess.PIPE)
        procs.append(p)

    last_time = 0
    curr_time = 0
    fd = open(conf)

    for i in range(0, 100):
        line = fd.readline()
        
        if not line:
            break
        
        rec = line.split(" ")
        if int(rec[0]) != 0:
            continue
        
        src = SRC_MAP[int(rec[0])]
        last_time = curr_time
        curr_time = float(rec[2])
        size = rec[3].strip()

        print line

        client_proc = procs[int(rec[0])]
        time.sleep(curr_time - last_time)
        #client_proc.stdin.write("python client.py %s 10087 %s\r\n" % (DST, size))
        client_proc.stdin.write("python client.py 192.168.5.22 10087 42423.32\n")

    for proc in procs:
        proc.kill()









