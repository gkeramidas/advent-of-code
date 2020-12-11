#!/usr/bin/env python3

# Before you leave, the Elves in accounting just need you to fix your
# expense report (your puzzle input); apparently, something isn't quite
# adding up.
#
# Specifically, they need you to find the two entries that sum to 2020
# and then multiply those two numbers together.

import sys


def find(numbers, goal):
    # For every list of numbers, we have to check the sum of first element
    # against all remaining ones, but then we can 'skip' the number we just
    # checked for the next iteration.
    if len(numbers) <= 1:
        raise ValueError("Cannot find a match")
    x = numbers[0]
    rest = numbers[1:]
    for y in rest:
        if x + y == goal:
            return x, y
    return find(rest, goal)


def main():
    numbers = [int(line) for line in sys.stdin.readlines()]
    try:
        x, y = find(numbers, 2020)
        print("x {} * y {} = {}".format(x, y, x * y))
    except ValueError:
        print("Could not find the answer")


if __name__ == '__main__':
    main()
    sys.exit(0)
