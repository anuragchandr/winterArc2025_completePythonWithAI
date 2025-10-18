# DAY 18 - Custom Exceptions in Python

## Overview

Custom exceptions let you represent application-specific error conditions clearly and handle them separately from built-in exceptions. They improve readability, make error handling more precise, and help surface meaningful messages and metadata for callers.

## Why create custom exceptions?

- Differentiate error types for clearer except blocks.
- Attach additional context (error codes, metadata).
- Encapsulate domain-specific validation and failure modes.

## Creating a simple custom exception

Example: define an exception that carries an optional code.

```python
class MyValueError(ValueError):
    def __init__(self, message="Input must be an integer or 'quit'.", code=None):
        super().__init__(message)
        self.code = code
```

## Example usage patterns

1) Input validation and raising a custom error:

```python
a = int(input("Enter any value between 5 and 9: "))
if a < 5 or a > 9:
    raise ValueError("Value should be between 5 and 9")
```

2) Robust loop that raises and handles a custom error (based on day18/customErrorClass.py):

```python
while True:
    user_input = input("Enter an integer (or type 'quit' to exit): ")
    if user_input.lower() == "quit":
        break
    try:
        x = float(user_input)
        if x % 1 != 0:
            raise MyValueError("Decimal numbers are not allowed.", code=1001)
        number = int(x)
        # use number...
    except MyValueError as mve:
        print(f"Custom error: {mve} (code={mve.code})")
    except ValueError:
        print("Invalid input. Please enter an integer or 'quit'.")
```

## Best practices

- Subclass a relevant built-in exception (ValueError, RuntimeError, etc.) rather than Exception when appropriate.
- Keep custom exceptions small and focused (message, optional code/context).
- Document when and why the exception is raised.
- Catch specific custom exceptions, not broad Exception, to avoid hiding bugs.

## When to prefer built-ins vs custom

- Use built-ins when they convey intent (ValueError, TypeError).
- Use custom exceptions when you need distinct handling or extra fields (error codes, remediation hints).

## Summary

Custom exceptions make error handling explicit and maintainable for application-specific rules. Define them simply, raise them where domain checks fail, and handle them explicitly so callers can respond appropriately.