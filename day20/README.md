# DAY 20

## Testing with pytest

### What is pytest?

- A simple and powerful testing tool for Python.
- Lets you write readable tests with plain assert statements and helpful failure output.

### Quick setup

- Install: pip install pytest
- Run all tests: pytest -q
- Run a single file: pytest db_test.py -q

### Files in this folder

- db_test.py — tests for a simple Database class (uses a fixture for setup/teardown).
- test_testing.py — basic function tests (add, divide) and an exception check.

### Key ideas (short)

- Assertions: use assert to check behavior.
- Fixtures: reusable setup/teardown for tests (e.g., creating a Database instance).
- Exception testing: use pytest.raises to verify errors are raised.

### Small tips

- Keep tests small and focused.
- Name test files and functions starting with test_ so pytest finds them.
- Run tests often while developing.

### Example (what you'll see)

- test_add_user ensures a user can be added and retrieved.
- test_divide checks normal division and that dividing by zero raises a ValueError.

