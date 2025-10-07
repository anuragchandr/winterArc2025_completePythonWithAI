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
    