# 1. for Loop
for i in range(3):
    print(f"For loop iteration: {i}")

# 2. while Loop
count = 0
while count < 3:
    print(f"While loop count: {count}")
    count += 1

# 3. break Statement
for i in range(5):
    if i == 3:
        break
    print(f"Break demo: {i}")

# 4. continue Statement
for i in range(5):
    if i == 2:
        continue
    print(f"Continue demo: {i}")
