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
    a_dic = {}
    b_dic = {}
    i = 1
    while i <= n:
        index = pow_mod_n(i, a, k)
        try:
            a_dic[index].add(i)
        except KeyError:
            a_dic[index] = set([i])
        i += 1
    j = 1
    while j <= n:
        index = pow_mod_n(j, b, k)
        try:
            b_dic[index].add(j)
        except KeyError:
            b_dic[index] = set([j])
        j += 1
    dic = {}
    for d in range(0 , k):
        try:
            for i in a_dic[d]:
                for j in b_dic[(k - d) % k]:
                    if i == j:
                        continue
                    dic[(i,j)] = (i,j)
        except KeyError:
            pass
    return len(dic)


def pow_mod_n(a, b, n):
    x, y = 1, a
    while b > 0:
        if b % 2 == 1:
            x = (x * y) % n
        y = (y * y) % n
        b /= 2
    return x % n

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
        a, b, n, k = long(temp[0]), long(temp[1]), long(temp[2]), int(temp[3])
        print "Case #%d: %d" % (index + 1, number_case(a, b, n, k))

