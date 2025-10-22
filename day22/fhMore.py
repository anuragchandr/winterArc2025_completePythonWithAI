f = open("poem.txt", 'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)

lines = ["When I was Five\n",
"I was just alive.\n",
"But now I am Six\n",
"I\'m as clever as clever\n",
"So I think I'll be six now for ever and ever.\n"]

f = open("poem.txt", "a")

f.writelines(lines)
f.close()