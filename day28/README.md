# DAY 28

## Virtual Environments & Dependency Management

Why it matters: Every serious Python project needs isolation and reproducibility. Learn to avoid "dependency hell" and keep projects clean and portable.

What is a virtual environment?

- An isolated Python runtime with its own site-packages.
- Prevents global package conflicts between projects.
- Tools: venv (built-in) and virtualenv (third-party).

Quick setup (Windows)

- Create: python -m venv env
- Activate (cmd): env\Scripts\activate
- Activate (PowerShell): .\env\Scripts\Activate.ps1
- Deactivate: deactivate

Managing packages with pip

- Install: pip install package_name
- Upgrade pip: python -m pip install --upgrade pip
- Uninstall: pip uninstall package_name

Requirements files

- Freeze current deps: pip freeze > requirements.txt
- Install from file: pip install -r requirements.txt
- Keep requirements.txt in repo; do NOT commit your env folder.

Key ideas

- Isolation: one env per project.
- Pin versions for reproducibility (e.g., package==1.2.3).
- Use a lock file or exact pins for production deployments.
- Prefer python -m venv to avoid PATH issues.
- Consider poetry or pipenv for higher-level dependency/lock management.

Best practices

- Add your env/ folder to .gitignore.
- Specify Python version in README or pyproject.toml.
- Use requirements.txt for simple projects; use lock files (poetry.lock, Pipfile.lock) for strict reproducibility.
- Regularly test install in a fresh env (CI helps).
- Keep dev and prod deps separate (extras or separate files like requirements-dev.txt).

Minimal workflow example (terminal)

```bash
python -m venv env
env\Scripts\activate
python -m pip install --upgrade pip
pip install requests==2.31.0
pip freeze > requirements.txt
deactivate

# On another machine / CI
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```
