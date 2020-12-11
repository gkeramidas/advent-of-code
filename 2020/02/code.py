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


def check2(t):
    m = re.match(r"^(\d+)-(\d+)\s+(\S): (.+)$", t)
    if not m:
        # Cannot invalid policy which does not parse.
        return False

    pa = int(m.group(1))
    pb = int(m.group(2))
    char = m.group(3)[0]
    password = m.group(4)

    # Positions pa and pb when converted to zero-based index *must* fall
    # within the bounds of len(password).
    pa -= 1
    pb -= 1
    if (
        pa < 0 or pa >= len(password) or
        pb < 0 or pb >= len(password)
    ):
        return False

    pair = [password[pa], password[pb]]
    count = len([c for c in pair if c == char])
    return count == 1


def main():
    lines = sys.stdin.readlines()
    valid = [check(t.rstrip('\n')) for t in lines]
    count = len([v for v in valid if v])
    print("{} valid lines".format(count))
    valid = [check2(t.rstrip('\n')) for t in lines]
    count = len([v for v in valid if v])
    print("{} valid lines".format(count))


if __name__ == '__main__':
    main()
    sys.exit(0)
