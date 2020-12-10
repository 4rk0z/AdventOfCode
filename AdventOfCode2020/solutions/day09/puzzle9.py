#!/usr/bin/env python3
from itertools import combinations

def isValid(number, before):
    if number < before:
        return None
    start_index = number - before
    if start_index < 0:
        start_index = 0
    comb = combinations(numbers[start_index:number], r=2)
    for i in comb:
        a, b = i
        if a + b == numbers[number]:
            status = True
            break
        else:
            status = False
    return status

def search(n):
    for i in range(0, n):
        last = n - i
        sum = 0
        c = 0
        while sum < numbers[n]:
            c += 1
            last -= 1
            sum += numbers[last]
            if sum == numbers[n]:
                return(last, n - i)
            elif sum > numbers[n]:
                continue
    return(None)

numbers = []
with open("input", "r", encoding="utf8") as f:
    lines = f.read()
for i in lines.strip().split():
    numbers += [int(i)]

# part1
before = 25
result = 0
for num in range(before, len(numbers)):
    if not isValid(num, before):
        result = num
print("part1:", numbers[result])

# part2
a, b = search(result)
f, l = sorted(numbers[a:b])[0], sorted(numbers[a:b])[-1]
print("part2:", f + l)
