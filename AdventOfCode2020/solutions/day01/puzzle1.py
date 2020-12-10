#!/usr/bin/env python3

from itertools import combinations

tab = []
with open("input", 'r', encoding="utf8") as input:
    for number in input:
        number = number[:-1]
        tab.append(int(number))


# part 1
comb_list = (list(combinations(tab, r=2)))
for i in comb_list:
    a, b = i
    if a + b == 2020:
        print("part1 :", a * b)

# part 2
comb_list = (list(combinations(tab, r=3)))
for i in comb_list:
    a, b, c = i
    if a + b + c == 2020:
        print("part2: ", a * b * c)
