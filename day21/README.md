# DAY 21

## Code style (PEP 8), Docstrings & Basic Debugging

What is PEP 8?

- The official style guide for Python code.
- Encourages readable, consistent code: meaningful names, indentation, line length, spacing.

Quick setup

- Install linters/formatters: pip install flake8 black pylint
- Auto-format: black .
- Check style: flake8 path/to/file.py

Files in this folder

- (Place code files here) — run linters and add docstrings to public functions and classes.

Key ideas (short)

- PEP 8 basics: 79-char line limit, 4-space indentation, snake_case for functions/vars, PascalCase for classes.
- Docstrings: add a clear one-line summary + short details for Args/Returns when needed.
- Debugging: start with prints, then use logging, pdb, or the VS Code debugger for breakpoints and stepping.

Small tips

- Use black for consistent formatting, flake8 to catch issues, and pylint for suggestions.
- Prefer logging over print for larger projects.
- Add docstrings when a function is part of your module's public API.
- Use breakpoint() or import pdb; pdb.set_trace() to inspect state interactively.

Example

- A small function with a docstring and a linter-friendly format.
- Run black and flake8 to fix/flag style issues.
- Use the VS Code debugger or breakpoint() to step through a failing case.
