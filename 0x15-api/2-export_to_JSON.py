#!/usr/bin/python3
"""
2-export_to_JSON.py

This script exports all tasks owned by a specified employee to a JSON file.
The file is named after the user ID and contains the following columns:
USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE.

Usage:
    python3 2-export_to_JSON.py <employee_id>

Arguments:
    <employee_id> (int): The ID of the employee.

Example:
    python3 2-export_to_JSON.py 2
"""

import json
import requests
import sys


def get_todo_list_progress(employee_id):
    """
    Fetches and exports tasks for a given employee ID to a JSON file.
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    # Fetch the username
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user = user_response.json()
    username = user.get('name')

    # Prepare data for JSON export
    data = {str(employee_id): []}
    for task in todos:
        task_entry = {
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        }
        data[str(employee_id)].append(task_entry)

    # Export data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID")
        sys.exit(1)

    get_todo_list_progress(employee_id)


if __name__ == "__main__":
    main()
