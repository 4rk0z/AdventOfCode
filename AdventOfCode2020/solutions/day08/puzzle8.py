#!/usr/bin/env python3

instructions = []
with open("input", "r", encoding="utf8") as f:
    lines = f.read()[:-1]
lines = lines.replace(":", " ").split('\n')
for i in lines:
    instructions += [i.split()]


def take_ins(nr):
    ins, arg = instructions[nr]
    return ins, int(arg)


def execute(ins_nr, ACC):
    global executed_ins
    if ins_nr == len(instructions):
        return ACC, True
    executed_ins.append(ins_nr)
    ins, arg = take_ins(ins_nr)
    if ins == "acc":
        ACC += arg
        next_ins = ins_nr + 1
    elif ins == "nop":
        next_ins = ins_nr + 1
    elif ins == "jmp":
        next_ins = ins_nr + arg
    if next_ins not in executed_ins:
        return execute(next_ins, ACC)
    return ACC, False  # false = not fixed

# part 1
executed_ins = []  # global
result, solved = execute(0, 0)
print("part1: ", result)

# part 2

suspected_ins = executed_ins.copy()
while len(suspected_ins) > 1:
    last = suspected_ins.pop()
    temp = instructions[last]
    ins, arg = temp
    if ins == "jmp":
        ins = "nop"
    elif ins == "nop":
        ins = "jmp"
    else:
        pass
    instructions[last] = (ins, arg)
    executed_ins = []  # global
    result, solved = execute(0, 0)
    if solved:
        print("part2: ", result)
        break
    else:
        instructions[last] = temp  # revert changes
