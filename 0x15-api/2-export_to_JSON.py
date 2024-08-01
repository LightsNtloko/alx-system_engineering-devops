#!/usr/bin/python3
"""
2-export_to_JSON.py

This script exports all tasks owned by a specified employee to a JSON file.
The file is named after the user ID and contains the following format:
{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
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

def get_employee_name(employee_id):
    """
    Fetches the employee's name for a given employee ID from the API.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    user = response.json()
    return user.get('name')

def get_todo_list(employee_id):
    """
    Fetches the TODO list for a given employee ID from the API.
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    return response.json()

def export_to_json(employee_id):
    """
    Exports the tasks of the given employee to a JSON file.
    """
    employee_name = get_employee_name(employee_id)
    todos = get_todo_list(employee_id)

    tasks = [
        {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": employee_name
        }
        for todo in todos
    ]

    data = {str(employee_id): tasks}

    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID")
        sys.exit(1)

    export_to_json(employee_id)
