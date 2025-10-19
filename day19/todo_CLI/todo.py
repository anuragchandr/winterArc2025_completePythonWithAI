tasks = []

def todo():
    while True:
        try:
            print("-------------------------\n TO DO CLI \n-------------------------")
            n = int(input("Choose action:\n1.Add Task\n2.Delete Task\n3.View Tasks\n4. Exit\n"))
            match n:
                case 1:
                    try:
                        element = input("Enter an task to add:")
                        tasks.append(element)
                    except Exception as e:
                        print(e)
                case 2:
                    if(len(tasks)==0):
                        print("No Tasks:")
                        continue
                    for i in range(len(tasks)):
                        print((i+1), tasks[i])
                    try:
                        rt = int(input("Enter task number to remove: ")) - 1
                        if 0 <= rt < len(tasks):
                            removed = tasks.pop(rt)
                            print(f" Task '{removed}' removed.")
                        else:
                            print("Invalid task number.")
                    except ValueError:
                        print("a" \
                        "Please enter a valid number.")
                case 3:
                    if(len(tasks)==0):
                        print("No Tasks:")
                        continue
                    for i in range(len(tasks)):
                        print(i+1, tasks[i])
                case 4:
                    return
        except Exception as e:  
            print(e)

if __name__ == "__main__":
    todo()