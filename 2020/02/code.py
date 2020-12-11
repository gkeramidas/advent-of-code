#!/usr/bin/env python

import sys
import re


def check(t):
    "1-3 a: abcde"
    m = re.match(r"^(\d+)-(\d+)\s+(\S): (.+)$", t)
    if not m:
        # Cannot invalid policy which does not parse.
        return False

    cmin = int(m.group(1))
    cmax = int(m.group(2))
    char = m.group(3)[0]
    password = m.group(4)

    count = len([c for c in password if c == char])
    return (cmin <= count and count <= cmax)


def main():
    lines = sys.stdin.readlines()
    valid = [check(t.rstrip('\n')) for t in lines]
    count = len([v for v in valid if v])
    print("{} valid lines".format(count))


if __name__ == '__main__':
    main()
    sys.exit(0)
