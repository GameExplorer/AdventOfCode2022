text = open('input_6.txt', 'r').read()

for i in range(len(text) - 4):
    if len(set(text[i:i + 4])) == 4:
        print(i + 4)
        break

for i in range(len(text) - 14):
    if len(set(text[i:i + 14])) == 14:
        print(i + 14)
        break
