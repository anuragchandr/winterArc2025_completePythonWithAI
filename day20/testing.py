#Testing in python using Pytest framework

def get_weather(temp):
    if temp > 30:
        return "It's a hot day"
    elif temp < 10:
        return "It's a cold day"
    else:
        return "It's a moderate day"

def add(a, b):
    return a + b

def divide(a, b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a / b