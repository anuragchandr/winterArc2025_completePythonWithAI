import requests
from pathlib import Path

TASKS_PATH = Path("tasks.txt")

def ensure_tasks_file():
    if not TASKS_PATH.exists():
        TASKS_PATH.write_text("", encoding="utf-8")

def read_tasks():
    ensure_tasks_file()
    with TASKS_PATH.open("r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.rstrip("\n")]

def write_tasks(tasks):
    with TASKS_PATH.open("w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def todo():
    while True:
        try:
            print(
                "-------------------------\n"
                "        TO DO CLI       \n"
                "-------------------------"
            )
            print("Choose action:\n1. Add Task\n2. Delete Task\n3. View Tasks\n4. Exit")
            choice = input("Enter choice (1-4): ").strip()
            if not choice:
                print("Please enter a choice.")
                continue
            try:
                n = int(choice)
            except ValueError:
                print("Invalid choice. Enter a number between 1 and 4.")
                continue

            if n == 1:
                element = input("Enter a task to add: ").strip()
                if not element:
                    print("Empty task not added.")
                    continue
                tasks = read_tasks()
                tasks.append(element)
                write_tasks(tasks)
                print("Task added.")
            elif n == 2:
                tasks = read_tasks()
                if not tasks:
                    print("No tasks to delete.")
                    continue
                show_tasks(tasks)
                rt_input = input("Enter task number to remove: ").strip()
                try:
                    rt = int(rt_input)
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                if 1 <= rt <= len(tasks):
                    removed = tasks.pop(rt - 1)
                    write_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            elif n == 3:
                tasks = read_tasks()
                show_tasks(tasks)
            elif n == 4:
                print("Goodbye.")
                return
            else:
                print("Choose a number between 1 and 4.")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting.")
            return
        except Exception as e:
            print("An error occurred:", e)


def quoteOfTheDay():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        quote = None
        author = None
        if isinstance(data, dict):
            if data.get("success") and "data" in data and isinstance(data["data"], dict):
                quote = data["data"].get("content")
                author = data["data"].get("author")
            else:
                # fallback keys
                quote = data.get("content") or data.get("quote")
                author = data.get("author")
        if quote:
            print(f'Quote of the Day:\n"{quote}"\n - {author or "Unknown"}\n')
        else:
            print("Failed to fetch quote of the day.")
    except requests.RequestException:
        print("Network error while fetching quote of the day.")
    except ValueError:
        print("Failed to parse quote response.")


if __name__ == "__main__":
    quoteOfTheDay()
    todo()
