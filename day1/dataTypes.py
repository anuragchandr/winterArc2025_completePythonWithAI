values = [42, 3.14, "hello", True, [1, 2], {"a": 1}, (3, 4), {1, 2}]

for val in values:
    print(f"{val} is of type {type(val)}")

print(f"type of values is object:{isinstance(values,object)} ")