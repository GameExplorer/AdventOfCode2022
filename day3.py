
print(sum(ord(c) - [64 - 26 , 96][c.islower()]
            for c in (next(iter(set(line[:len(line) // 2]) & set(line[len(line) // 2:])))
                        for line in open("input_3.txt"))))

it = iter(open("input_3.txt"))
print(sum(ord(c) - [64 - 26, 96][c.islower()]
            for c in
            (next(iter(set(line.strip()) & set(next(it)) & set(next(it))))
                for line in it)))

