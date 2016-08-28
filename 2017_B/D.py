# !/usr/bin/env python
# coding=utf-8

import sys
from itertools import permutations

def permutation_sorting(n, m):
    all_list = list(permutations(range(1, n + 1)))
    for l in all_list:


def computer_chunks(l, start, end):
    count = 0
    lmax, rmin = -1, -1
    start += 1
    while start < end:
        if lmax == -1:
            lmax = l[start]
            rmin = minmin(l[start + 1:end + 1])
            start += 1
        if lmax < rmin:
            count += 1
            lmax = -1
        else:
            if lmax < l[start]:
                lmax = l[start]
            rmin = minmin(l[start + 1:end + 1])
        start += 1
    return count







if __name__ == '__main__':
    # begin
    open_file = open("../test.in", 'rU')
    sys.stdout = open("../test.out", 'w')
    input_parameters = open_file.read().split('\n')
    num_case = int(input_parameters[0])
    pos = 1
    for index in range(num_case):
        temp = input_parameters[pos].split(' ')
        n, m = int(temp[0]), int(temp[1])
        pos += 1
        print "Case #%d: %d" % (index + 1, permutation_sorting(n, m))
