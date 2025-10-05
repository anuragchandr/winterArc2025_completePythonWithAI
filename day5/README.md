# DAY 5

## Functions in Python

Functions are reusable blocks of code that perform a specific task. They help organize code into logical sections and improve readability.

### 🔹 Defining a Function

Use the `def` keyword followed by the function name and parentheses:

```python
def greet(name):
    return "Hello " + name
```

## Parameters

- Parameters are variables listed inside the parentheses in a function definition.
- They allow functions to accept input values and make the function dynamic.

### Example:

```python
def add(a, b):
    return a + b
```

## Return Statement

- The return statement sends a result back to the caller.

- It ends the function’s execution and outputs a value.

### Example

```python
def square(x):
    return x * x
```

## Scope

Scope defines the visibility and lifetime of variables in Python.

- **Local Scope**: Variables declared inside a function; accessible only within that function.
- **Global Scope**: Variables declared outside any function; accessible throughout the program.

### Example:

```python
x = 10  # global variable

def show():
    y = 5  # local variable
    print(x + y)
