#!/usr/bin/env python3

import string

with open("input", "r", encoding="utf8") as f:
    lines = f.read()

groups = lines.split("\n\n")

# part 1
sum = 0
for group in groups:
    group = group.replace('\n', '')
    group = set(group)
    sum += len(group)
print("part1: ", sum)

# part 2


def initFullSet():
    x = {*()}
    for char in string.ascii_lowercase:
        x.add(char)
    return x


_full_set_ = initFullSet()

sum = 0
for group in groups:
    group = group.split()
    sum += len(_full_set_.intersection(*group))
print("part2: ", sum)
