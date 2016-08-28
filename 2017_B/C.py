# !/usr/bin/env python
# coding=utf-8

import sys



if __name__ == '__main__':
    # begin
    open_file = open("../test.in", 'rU')
    sys.stdout = open("../test.out", 'w')
    input_parameters = open_file.read().split('\n')
    num_case = int(input_parameters[0])
    pos = 1
    for index in range(num_case):
        temp = input_parameters[pos].split(' ')
        pos += 1
        n = int(temp[0])
        m = int(temp[1])
        size = []
        temp = input_parameters[pos].split(' ')
        pos += 1
        for i in range(n):
            size.append(int(temp[i]))
        query = []
        print "Case #%d:" % (index + 1)
        for i in range(m):
            temp = input_parameters[pos].split(' ')
            # pdb.set_trace()
            print "%0.9f" % gcube(size, int(temp[0]), int(temp[1]))
            pos += 1
