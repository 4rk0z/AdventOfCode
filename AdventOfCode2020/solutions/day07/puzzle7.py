#!/usr/bin/env python3
import string

colours_set = {*()}  # global part 1
required_bags = 0  # global part 2


def search(anchor):
    global colours_set
    for key, value in rules_dict.items():
        if anchor in value:
            search(key)
            colours_set.add(key)
    return(len(colours_set))


def separate(str):
    n = 0
    for i in str:
        if not i.isdigit():
            return str[:n], str[n:]
        n += 1
    return 0, None


def solve(anchor):
    global required_bags
    c, l = separate(anchor)
    for i in rules_dict[l].split(","):
        if i == "0False":
            return()
        else:
            c_prim, none = separate(i)
            required_bags += (int(c.strip()) * int(c_prim.strip()))
            for j in range(int(c.strip())):
                solve(i)
    return required_bags


def replace_all(text, dict):
    for i, j in dict.items():
        text = text.replace(i, j)
    return text


with open("input", "r", encoding="utf8") as f:
    lines = f.read()[:-1]

to_replace = {
    " bags contain ": ":",
    "bags": "",
    "bag": "",
    "no other": "0False",
    ".": "",
    " ": ""}
rules = replace_all(lines, to_replace)
rules = rules.split("\n")
rules_dict = {}
for rule in rules:
    x = rule.find(":")
    rules_dict.update({rule[:x]: rule[x + 1:]})


# part 1
print(search("shinygold"))

# part 2
print(solve("1shinygold"))
