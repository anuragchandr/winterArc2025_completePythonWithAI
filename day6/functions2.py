# (*args)
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_all(1, 2, 3, 4, 5))  # Output: 15

# (**kwargs)
def display_info(name, age, **info):
    print(f"Name: {name}, Age: {age}")
    for key, value in info.items():
        print(f"{key}: {value}")

display_info("Alice", 30, city="New York", job="Engineer")

# Default parameters
def multiply(x, y=2):
    return x * y

print(multiply(5))      # Output: 10
print(multiply(5, 3))   # Output: 15

#lambda function

double = lambda x: x * 2
print(double(5))  # Output: 10

avg = lambda a, b: (a + b) / 2
print(avg(4, 6))  # Output: 5.0

def apply_function(func, value):
    return func(value)
print(apply_function(lambda x: x ** 2, 4))  # Output: 16

