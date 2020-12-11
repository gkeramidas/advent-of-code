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


def find3(numbers, goal):
    # For more than two 'dimensions' it's better to generate the
    # triangular part of the NxNxN cube of all possible numbers, and
    # just check the triplets.
    def triplets(numbers):
        size = len(numbers)
        for ix in range(size):
            for iy in range(ix + 1, size):
                for iz in range(iy + 1, size):
                    yield numbers[ix], numbers[iy], numbers[iz]

    if len(numbers) <= 2:
        raise ValueError("Cannot find a match")
    for x, y, z in triplets(numbers):
        if x + y + z == goal:
            return x, y, z
    raise ValueError("No match found")


def main():
    numbers = [int(line) for line in sys.stdin.readlines()]
    try:
        x, y = find(numbers, 2020)
        print("x {} * y {} = {}".format(x, y, x * y))
    except ValueError as e:
        print(e)
    try:
        x, y, z = find3(numbers, 2020)
        print("x {} * y {} * z {} = {}".format(x, y, z, x * y * z))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
    sys.exit(0)
