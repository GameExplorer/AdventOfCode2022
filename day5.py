from copy import deepcopy

lines, instructions = open("input_5.txt").read().split("\n\n")
lines = lines.splitlines()
stacks = {lines[-1][column]: [lines[row][column]
                              for row in range(len(lines) - 2, -1, -1)
                              if len(lines[row]) > column and lines[row][column] != " "]
          for column in range(1, len(lines[-1]), 4)}

stacks2 = deepcopy(stacks)

for _, quantity, _, source, _, destination in map(str.split, instructions.strip().splitlines()):
    quantity = int(quantity)

    # Part 1
    stacks[destination] += stacks[source][-1:-quantity - 1:-1]
    del stacks[source][-quantity:]

    # Part 2
    stacks2[destination] += stacks2[source][-quantity:]
    del stacks2[source][-quantity:]

print("".join(stack[-1] for stack in stacks.values()))
print("".join(stack[-1] for stack in stacks2.values()))