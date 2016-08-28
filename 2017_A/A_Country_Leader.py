# !/usr/bin/env python
# coding=utf-8
import sys

class Leader(object):

    def __init__(self, name):
        self.name = name
        self.diff = len(set(name.replace(' ', '')))

    def __cmp__(self, other):
        if self.diff != other.diff:
            return cmp(self.diff, other.diff)
        return cmp(other.name, self.name)


def Country_Leader(names):
    ls = len(names)
    res = [Leader(name) for name in names]
    res.sort()
    # print [r.diff for r in res]
    # print [r.name for r in res]
    # print [r.after_name for r in res]
    return res[-1].name


if __name__ == '__main__':
    # read number of cases
    open_file = open("../test.in", 'rU')
    sys.stdout = open("../test.out", 'w')
    input_parameters = open_file.read().split('\n')
    num_case = int(input_parameters[0])
    pos = 1
    # read case
    for index in range(num_case):
        num_lines = int(input_parameters[pos])
        pos += 1
        names = []
        for i in range(num_lines):
            names.append(input_parameters[pos])
            pos += 1
        # output
        print "Case #%d: %s" % (index + 1, Country_Leader(names))