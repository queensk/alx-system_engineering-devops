#!/usr/bin/python3
"""
For a given employee ID, returns information about
their TODO list progress
"""

import requests


def get_todo_list_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    # Count number of completed tasks
    completed_tasks = [task for task in todos if task['completed'] is True]
    total_tasks = len(todos)
    completed_task_count = len(completed_tasks)

    # Get employee name
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    employee_name = user_response.json()['name']

    # Print results
    print(
        f"Employee {employee_name} is done with tasks({completed_task_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    import sys
    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)
