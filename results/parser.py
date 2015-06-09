__author__ = 'v-whao'


import sys
import os

def usage():
    print "python parser.py path    //path could be a file or a directory"


def cal(file_path):
    results = []

    with open(file_path) as fd:
        for line in fd.readlines():
            if line.strip():
                l_items = line.split(" ")
                size = int(l_items[4])
                duration = float(l_items[-1])

                if duration > 3:    # filter out abnormal duration
                    continue

                results.append((size, duration))
            else:
                continue

    # results_sorted = sorted(results, key=lambda rec: rec[0])

    # (0, 100KB)
    zero_to_hundred = filter(lambda rec: rec[0] < 102400, results)
    # (100KB, 10MB)
    kb_to_mb = filter(lambda rec: 102400 <= rec[0] < 10485760, results)
    # (10MB, infi)
    mb_to_infi = filter(lambda rec: rec[0] >= 10485760, results)

    print "AVERAGE FCT is:"
    print "(0, 100KB):     \t", average(zero_to_hundred)
    print "(0, 100KB) 99tile: \t", \
        average(sorted(zero_to_hundred,
                       key=lambda rec: rec[0])[int(len(zero_to_hundred)*0.99):])
    print "[100KB, 10MB):     \t", average(kb_to_mb)
    print "[10MB, infi):     \t", average(mb_to_infi)


def average(input_tuple_list):
    input_list = [x[1] for x in input_tuple_list]
    return sum(input_list) / len(input_list)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        usage()
        exit(0)

    path = sys.argv[1]

    if os.path.isfile(path):
        cal(path)
    elif os.path.isdir(path):
        for f in os.listdir(path):
            if os.path.splitext(f)[1] == '.txt':
                cal(f)
            else:
                continue
    else:
        print "invalid parameters, please input a path"
