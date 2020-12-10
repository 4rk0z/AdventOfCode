#!/usr/bin/env python3

import re


def isValid(seat):
    def check(x): return bool(re.match(r"^[FB]{7}[LR]{3}$", x))
    return check(seat)


def decode_seat_nr(seat_code):
    if isValid(seat_code):
        row, col = seat_code[:7].translate(str.maketrans(
            'FB', '01')), seat_code[-3:].translate(str.maketrans('LR', '01'))
        row = (int(row, 2))
        col = (int(col, 2))
        return row, col
    else:
        return None, None


def encode_seat_nr(row, col):
    if row in range(0, 128) and col in range(0, 8):
        seat_code = "{0:{fill}7b}".format(
            row, fill='0').translate(
            str.maketrans(
                '01', 'FB')) + "{0:{fill}3b}".format(
                col, fill='0').translate(
                    str.maketrans(
                        '01', 'LR'))
        return(seat_code)
    return None


seats = []

with open("input", 'r', encoding="utf8") as input:
    for line in input:
        line = line[:-1].strip()
        seats += line.split()


# part 1
min_seat_id = 127 * 8 + 7
max_seat_id = 0 * 8 + 0
for i in seats:
    row, col = decode_seat_nr(i)
    seat_id = row * 8 + col
    if seat_id > max_seat_id:
        max_seat_id = seat_id
    if seat_id < min_seat_id:
        min_seat_id = seat_id
print("part1: ", max_seat_id)


# part 2
for i in range(min_seat_id // 8, max_seat_id // 8):
    for j in range(0, 8):
        if encode_seat_nr(i, j) not in seats:
            print("part2: ", i * 8 + j)
