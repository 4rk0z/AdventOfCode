#!/usr/bin/env python3

def walk(x, y):
    row = col = 0
    moves = 0
    while row < pattern_row_nums - 1:
        col = (col + x) % pattern_col_nums
        row += y
        if pattern[row][col] == '#':
            moves += 1
    return moves


pattern = []
pattern_col_nums = pattern_row_nums = 0

with open("input", 'r', encoding="utf8") as input:
    for lines in input:
        lines = lines[:-1]
        pattern += lines.split()

pattern_col_nums = len(pattern[0])
pattern_row_nums = len(pattern)

# part 1
print("part1:", walk(3, 1))

# part 2
print("part2:", walk(1, 1) * walk(3, 1) * walk(5, 1) * walk(7, 1) * walk(1, 2))
