# DAY 17 


## `try`, `except`, and `finally` Blocks

Error handling is a critical aspect of writing reliable and user-friendly Python applications. This section dives into the fundamental `try`, `except`, and `finally` blocks, demonstrating how to gracefully manage potential errors without crashing your program.

### 🔹 The `try` Block

The `try` block is where you place the code that might potentially raise an exception. Python attempts to execute the code within this block.

-   If an exception occurs during the execution of the `try` block, the normal flow is interrupted, and Python looks for a matching `except` block.
-   If no exception occurs, the `except` block(s) associated with this `try` are skipped.

### Example: Handling Potential `ValueError` in a Multiplication Table

```python
a = input("Enter a Number:")
print(f"Multiple table of {a} is: ")

try:
    # This loop attempts to convert 'a' to an integer and perform multiplication.
    # If 'a' cannot be converted (e.g., if it's text), a ValueError will occur here.
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
    print("Some imp lines of Code") # This line executes only if no exception occurs in the try block