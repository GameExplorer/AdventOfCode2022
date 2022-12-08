ls = []
for raw_line in open("input_7.txt", "r"):
    ls.append(raw_line.replace('\n', ''))

gsm = 0
best = None
bestSize = 1000000000


class folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def __repr__(self):
        return self.name + " " + str(self.files) + " " + str(self.children)

    def solve(self):
        global gsm, best, bestSize
        self.w = sum([x[1] for x in self.files])
        for child in self.children:
            child.solve()
            self.w += child.w
        if self.w <= 100000:
            gsm += self.w
        if self.w >= 528671 and self.w < bestSize:
            best = self
            bestSize = self.w
        # print(self.name, self.w)


f = folder("/", None)
root = f
i = 1
while i < len(ls):
    l = ls[i].split()
    if l[0] == "$":
        if l[1] == "ls":
            for j in range(i + 1, len(ls)):
                if ls[j][0] == "$":
                    break
            else:
                j = len(ls)
            for k in range(i + 1, j):
                # print(ls[k])
                a, b = ls[k].split()
                if a == "dir":
                    f.children.append(folder(b, f))
                else:
                    a = int(a)
                    f.files.append((b, a))
            i = j - 1
        elif l[1] == "cd":
            if l[2] == "..":
                f = f.parent
            else:
                for child in f.children:
                    if child.name == l[2]:
                        f = child
                        break
                else:
                    assert False
        else:
            assert False
    else:
        # print(l)
        assert False
    i += 1

# print(root)

root.solve()
print(gsm)

space = 70000000
free_needed = 30000000

print(root.w)
print(space - root.w)
print(free_needed - (space - root.w))

print(best.w, best.name)