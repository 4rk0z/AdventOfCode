#!/usr/bin/env python3

import re


def isValid(p, status=False):
    if (p.count('byr') & p.count('iyr') & p.count('eyr') & p.count('hgt')
            & p.count('hcl') & p.count('ecl') & p.count('pid')):
        status = True
    return status


def isMatch(p):
    for i, j in zip(p[0::2], p[1::2]):
        if not (rules[i](j) and values[i](j)):
            return False
    return True


def isHeightValid(height):
    check = {
        "cm": lambda x: 150 <= int(x) <= 193,
        "in": lambda x: 59 <= int(x) <= 76,
    }
    height, unit = height[:-2], height[-2:]
    return check[unit](height)


values = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": isHeightValid,
    "hcl": lambda x: True,
    "ecl": lambda x: True,
    "pid": lambda x: True,
    "cid": lambda x: True,
}


rules = {
    "byr": lambda x: bool(re.match(r"^\d{4}$", x)),
    "iyr": lambda x: bool(re.match(r"^\d{4}$", x)),
    "eyr": lambda x: bool(re.match(r"^\d{4}$", x)),
    "hgt": lambda x: bool(re.match(r"^\d{2}in$|^\d{3}cm$", x)),
    "hcl": lambda x: bool(re.match(r"^#[a-f0-9]{6}$", x)),
    "ecl": lambda x: bool(re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", x)),
    "pid": lambda x: bool(re.match(r"^\d{9}$", x)),
    "cid": lambda x: True,
}


passports = []
with open("input", "r", encoding="utf8") as f:
    lines = f.read()

lines = lines.replace(":", " ").split('\n\n')
for i in lines:
    passports += [i.split()]

# part 1 & 2

nvp = np_pvar = 0

for i in passports:
    if isValid(i):
        nvp += 1
    if isValid(i) and isMatch(i):
        np_pvar += 1

# nvp - number of valid passports - those that have all required fields
print("part 1: ", nvp)
# np_pvar -number of passports where all required fields are both present
# and valid according to the above rules
print("part 2: ", np_pvar)
