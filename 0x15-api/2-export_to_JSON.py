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


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(user_id))
    if user_response.status_code != 200:
        print("Error fetching user data")
        sys.exit(1)
    user = user_response.json()

    username = user.get("username")

    todos_response = requests.get(url + "todos", params={"userId": user_id})
    if todos_response.status_code != 200:
        print("Error fetching TODO data")
        sys.exit(1)
    todos = todos_response.json()

    tasks = []
    for todo in todos:
        tasks.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        })

    data = {user_id: tasks}

    json_filename = "{}.json".format(user_id)
    with open(json_filename, "w") as jsonfile:
        json.dump(data, jsonfile)

    print("Data successfully written to", json_filename)
