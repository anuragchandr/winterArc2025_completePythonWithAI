# DAY7

## TO-DO App

### Description

This is a simple command-line Task Manager built in Python using the match-case statement (introduced in Python 3.10). It allows users to add, delete, and view tasks interactively.

#### Features

- ✅ Add new tasks

- 🗑️ Delete existing tasks by name

- 📋 View all tasks with their index

- 🚪 Exit the program

### Concepts Used

- match-case (Python 3.10+)

- while loop for continuous interaction

- list operations (append, remove)

- range() and len() for index-based iteration

### Code snippet

 ``` python

    tasks = []
    while True:
        n = int(input("Choose action:\n1.Add Task\n2.Delete Task\n3.View Tasks\n4. Exit"))
        match n:
            case 1:
                element = input("Enter an task to add:")
                tasks.append(element)
            case 2:
                for i in range(len(tasks)):
                    print((i+1), tasks[i])
                rt = input("    :enter task to remove")
                tasks.remove(rt)
            case 3:
                for i in range(len(tasks)):
                    print(i, tasks[i])
            case 4:
                break
        
```
