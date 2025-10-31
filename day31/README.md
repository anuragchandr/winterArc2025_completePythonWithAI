<span style="color:pink;">
# DAY 31

## Setting UP the DATA Science Basecamp

### __Initilizing Virtual Environment__

- Create: python -m venv env
- Activate (cmd): 
```bash
env\Scripts\activate
```
- Activate (PowerShell): .<mark>\env\Scripts\Activate.ps1</mark>
- Deactivate: deactivate

### Setting Up Jupyter-Notebook

Quick goal: run notebooks inside your project venv so code uses the correct packages.

Install inside your venv (Windows terminal / PowerShell)
```bash
env\Scripts\activate            # cmd or PowerShell: activate your venv
python -m pip install --upgrade pip
pip install jupyter ipykernel
```

Register the venv as a notebook kernel (so Jupyter / VS Code can pick it)
```bash
python -m ipykernel install --user --name=myenv --display-name="Python (myenv)"
```

Run Jupyter
- Notebook: jupyter notebook
- Lab (nicer UI): pip install jupyterlab && jupyter lab

Basic workflow
- Create a new .ipynb, choose the "Python (myenv)" kernel.
- Run cells with Shift+Enter. Use Esc + M to toggle a cell to Markdown.
- Restart kernel if state is stale (Kernel -> Restart).

Handy tips
- Use %pip install package in a notebook cell to install into the active kernel (preferred over !pip).
- Save notebooks to the project folder; avoid committing large outputs. Add .ipynb_checkpoints/ and env/ to .gitignore.
- Use nbstripout or jupyter --no-browser and lightweight tools (nbconvert, nbdime) to keep diffs clean.
- For reproducibility, keep requirements.txt up to date:
  python -m pip freeze > requirements.txt

VS Code notes
- Open the folder, open a .ipynb or use the Interactive Window.
- Select the correct kernel from the top-right kernel picker.
- VS Code lets you run cells inline and debug cells with breakpoints.


</span>