#!/usr/bin/env python3

matched_part1 = matched_part2 = 0
with open("input", 'r', encoding="utf8") as input:
    for policy in input:
        policy = policy[:-1].replace(":", "")
        min, max, char, password = policy.replace("-", " ").split()
        if password.count(char) in range(int(min), int(max) + 1):
            matched_part1 += 1
        first, second = min, max
        if ((password[int(first) - 1] == char) ^
                (password[int(second) - 1] == char)):
            matched_part2 += 1

print("part1: ", matched_part1)
print("part2: ", matched_part2)
