import re

pairs = [[int(x) for x in re.findall("\\d+", line)] for line in open("input_4.txt")]
print(sum(x0 <= y0 <= y1 <= x1 or y0 <= x0 <= x1 <= y1 for x0, x1, y0, y1 in pairs))
print(sum(x0 <= y0 <= x1 or y0 <= x0 <= y1 for x0, x1, y0, y1 in pairs))