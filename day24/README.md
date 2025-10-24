# DAY 24

## Command-line Interfaces with argparse

A short, human-friendly guide to building simple CLI tools using Python's built-in argparse.

What is argparse?
- Part of the Python standard library for parsing command-line arguments.
- Lets you define positional and optional arguments, auto-generates help text, and validates input.

Quick setup
- No install needed (argparse is in the standard library).
- Run your script from the terminal: python script.py <args>

Files in this folder
- parsesrrs.py — small demo showing positional numbers and an optional --operation argument.

Key ideas (short)
- Positional arguments: required, order matters (e.g., number1, number2).
- Optional arguments: start with -- or - (e.g., --operation), can have defaults.
- Types: use type=int to auto-convert and validate input.
- Choices: restrict allowed values (e.g., choices=["add","sub","mul","div"]).
- Help: argparse auto-creates -h/--help from your add_argument help strings.
- parse_args() returns a Namespace (access via args.number1, args.operation).

Small tips
- Use type=int so you don't need manual int() conversions.
- Use choices to avoid manual validation of operations.
- Provide clear help text for each argument.
- For complex CLIs, consider subparsers (subcommands) or click/typer for nicer ergonomics.

Usage examples (terminal)
- Required positional args:
  python parsesrrs.py 4 5 --operation add
- Help:
  python parsesrrs.py -h

Example (what you'll see)
- prints args.number1 and args.number2, then performs the chosen operation:
  - add -> sum
  - sub -> subtraction
  - mul -> multiplication
  - div -> division (watch for ZeroDivisionError)

Minimal example snippet
```python
import argparse

parser = argparse.ArgumentParser(description="Simple calculator")
parser.add_argument("number1", type=int, help="first number")
parser.add_argument("number2", type=int, help="second number")
parser.add_argument("--operation", choices=["add","sub","mul","div"],
                    default="add", help="operation to perform")
args = parser.parse_args()

n1, n2 = args.number1, args.number2
if args.operation == "add":
    print("result:", n1 + n2)
# handle other ops similarly
```

That's it — define clear arguments, use types/choices, and rely on argparse to give users helpful error messages and documentation.