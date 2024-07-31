#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

This script fetches and displays the TODO list progress for a given employee ID
using a REST API. It displays the employee's name, the number of completed
tasks, and the total number of tasks. It also lists the titles of the completed
tasks.

Usage:
    ./0-gather_data_from_an_API.py <employee_id>

Arguments:
    <employee_id> (int): The ID of the employee.

Example:
    ./0-gather_data_from_an_API.py 1
"""

import sys
import requests


def fetch_employee_todo_list(employee_id):
    """
    Fetches the TODO list for a given employee ID from the API.
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    return response.json()


def main():
    """
    Main function to fetch and display the TODO list progress.
    """
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID")
        return

    todos = fetch_employee_todo_list(employee_id)
    if not todos:
        print("No data found for employee ID {}".format(employee_id))
        return

    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])

    # Placeholder, replace with actual name if available
    employee_name = f"Employee {employee_id}"

    print(f"Employee {employee_name} is done with tasks({done_tasks}/
            {total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"     {todo['title']}")


if __name__ == "__main__":
    main()
