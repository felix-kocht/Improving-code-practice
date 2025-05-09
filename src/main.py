from file_io import load_file, save_file
from task import Task
from task_manager import add_element, create_element


def interact():
    tasklist = load_file("data/tasklist_data.json")
    print("Welcome to the CLI Task Manager!")

    while True:
        name, year, month, day, completed = get_user_input()

        if name.lower() == "exit":
            print("Exiting Task Manager. Goodbye!")
            save_file("data/tasklist_data.json", tasklist)
            break

        name, year, month, day, completed_flag = parse_user_input(
            name, year, month, day, completed
        )
        task = create_element(name, year, month, day, completed_flag)
        add_element(task, tasklist)
        display_tasklist(tasklist)


def get_user_input():
    """
    Prompt the user for task details and return them.
    """
    name = input("Enter task name: ").strip()

    year = input("Enter due year (or leave blank): ").strip()
    month = input("Enter due month (or leave blank): ").strip()
    day = input("Enter due day (or leave blank): ").strip()

    completed = input("Is the task completed? (y/n): ").strip().lower()

    return name, year, month, day, completed


def parse_user_input(name, year, month, day, completed):
    """
    Parses user input into the correct types expected by create_element.
    """
    year = int(year) if year else None
    month = int(month) if month else None
    day = int(day) if day else None
    completed_flag = True if completed == "y" else False

    return name, year, month, day, completed_flag


def display_tasklist(tasklist):
    """
    Displays all tasks currently in the list.
    """
    print("\nCurrent Tasks:")
    for idx, task in enumerate(tasklist, start=1):
        display_element(task, idx)


def display_element(element: Task, number: int):
    print(str(number) + " - " + str(element))


def main():
    """
    Entry point for the CLI application.
    """
    interact()


if __name__ == "__main__":
    main()
