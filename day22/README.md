# DAY 22

## File Handling In Python

### In TXT file

- __Read__ :

```python
    m = open('myfile.txt', 'r') # r for read mode(its also default)
    text = m.read()
    print(text)
    m.close()
```

- __Write__ :

```python
    f = open('myfile2.txt','w') #write Mode(it overwrites but to append text we use append mode )
    f.write("Hello World")
    f.close()
    #f.truncate(5)
    f = open('myfile2.txt', 'a')
    f.write("Hello World")
    f.close()

    with open("myfile2.txt", 'a') as f:
        f.write("Hello")
```

## More file handling topics 

### Quick summary of open() modes

- 'r'  : read (default) — file must exist.
- 'w'  : write — creates/overwrites file.
- 'a'  : append — creates file if missing, writes at end.
- 'x'  : exclusive create — fails if file exists.
- 'b'  : binary mode (e.g., 'rb', 'wb').
- 't'  : text mode (default).
- '+'  : update (read and write), e.g., 'r+'.

### Context manager (preferred)

- Use with open(...) as f: to auto-close files even on errors:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")
# file auto-closed here
```

### Reading methods

- f.read()       — read whole file (careful with large files).
- f.readline()   — read one line at a time.
- f.readlines()  — return a list of lines.
- iterate file   — for line in f: is memory-friendly.

### Writing methods

- f.write(string)   — write a string.
- f.writelines(list) — write a list of strings (no newlines added automatically).

### Binary files

- Open images, audio, pickles in binary mode:

```python
with open("img.png", "rb") as f:
    data = f.read()
```

### __seek()__ and __tell()__

- f.seek(offset, whence=0) — move file pointer.
- f.tell() — current position.
- See fhadv.py for examples (seek(10), tell(), read(5)).

### Encoding

- Always set encoding when reading/writing text to avoid surprises:
  encoding="utf-8" is recommended.

### File existence & helpers

- os.path.exists(path) to check existence.
- os.remove(path) to delete.
- Prefer pathlib.Path for modern path handling:

```python
from pathlib import Path
p = Path("data.txt")
if p.exists():
    text = p.read_text(encoding="utf-8")
```
