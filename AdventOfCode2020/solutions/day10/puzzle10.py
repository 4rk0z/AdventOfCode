#!/usr/bin/env python3

with open("input", "r", encoding="utf8") as f:
    adapters = [int(lines) for lines in f.readlines()]

adapters.append(0)                 # charging outlet near seat (effective joltage rating of 0)
adapters = (sorted(adapters))
adapters.append(adapters[-1] + 3)  # built-in joltage adapter (effective joltage +3 jolts higher than the highest-rated adapter)


# part1
d1, d3 = 0, 0
for a, b in zip(adapters[0::1], adapters[1::1]):
    diff = b - a
    if diff == 1:
        d1 += 1
    elif diff == 3:
        d3 += 1
    else:
        raise ValueError("diff not equal to 1 or 3!")
print("part1:", d1 * d3)


# part2
total = {}
for adapter in adapters:
    total[adapter] = 0  # init with zeroes
total[0] = 1  # set entry point
for a in adapters:
    for i in range(1, 4):
        if a - i in total:
            total[a] += total[a - i]

print("part2:", list(total.values())[-1])
