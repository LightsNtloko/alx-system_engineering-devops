#!/usr/bin/python3
"""
1-export_to_CSV.py

This script fetches and exports the TODO list progress for a given employee ID
using a REST API. It exports the employee's tasks to a CSV file and validates
the number of tasks in the CSV file.

Usage:
    ./1-export_to_CSV.py <employee_id>

Arguments:
    <employee_id> (int): The ID of the employee.

Example:
    ./1-export_to_CSV.py 1
"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    user_url = url + "users/{}".format(user_id)
    print("Fetching user data from:", user_url)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error fetching user data")
        sys.exit(1)
    user = user_response.json()
    print("User data:", user)

    username = user.get("username")
    print("Username:", username)

    todos_url = url + "todos"
    print("Fetching TODO list from:", todos_url)
    todos_response = requests.get(todos_url, params={"userId": user_id})
    if todos_response.status_code != 200:
        print("Error fetching TODO data")
        sys.exit(1)
    todos = todos_response.json()
    print("TODO list:", todos)

    csv_filename = "{}.csv".format(user_id)
    print("Writing to CSV file:", csv_filename)
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([
                user_id,
                username,
                todo.get("completed"),
                todo.get("title")
            ])
    print("Data successfully written to", csv_filename)
