# !/usr/bin/env python
# coding=utf-8

import sys

# def number_case(a, b, n, k):
#     count = 0
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if i == j:
#                 continue
#             if (pow_mod_n(i, a, k) + pow(j, b, k)) % k == 0:
#                 count += 1
#     return count

def number_case(a, b, n, k):
    count = 0
    a_dic = {}
    b_dic = {}
    for i in range(1, n + 1):
        index = pow_mod_n(i, a, k)
        try:
            a_dic[index].add(i)
        except KeyError:
            a_dic[index] = set([i])
    for j in range(1, n + 1):
        index = pow_mod_n(j, b, k)
        try:
            b_dic[index].add(j)
        except KeyError:
            b_dic[index] = set([j])
    for d in range(0 , k):
        try:
            count += len(a_dic[d]) * len(b_dic[(k - d) % k])
            count -= len(a_dic[d].intersection(b_dic[(k - d) % k]))
        except KeyError:
            pass
    return count


def pow_mod_n(a, b, n):
    x, y = 0, a % n
    while b > 0:
        if b % 2 == 1:
            x = (x + y) % n
        y = (y * 2) % n
        b /= 2
    return x % n

def number_case(a, b, n, k):
    a_dic = {}
    b_dic = {}
    count = 0
    for i in range(1, n + 1):
        curr = pow(i, a)
        try:
            a_dic[curr % k].add(i)
        except KeyError:
            a_dic[curr % k] = set([i])

    for j in range(1, n + 1):
        curr = pow(j, b)
        try:
            b_dic[curr % k].add(j)
        except KeyError:
            b_dic[curr % k] = set([j])
    for d in range(0, k):
        try:
            count += len(a_dic[d]) * len(b_dic[(k - d) % k])
            count -= len(a_dic[d].intersection(b_dic[(k - d) % k]))
        except KeyError:
            pass
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
        pos += 1
        a, b, n, k = int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3])
        print "Case #%d: %d" % (index + 1, number_case(a, b, n, k))

