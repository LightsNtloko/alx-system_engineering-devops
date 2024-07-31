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


def fetch_employee_name(employee_id):
    """
    Fetches the employee's name for a given employee ID from the API.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    user = response.json()
    return user.get('username')


def fetch_employee_todo_list(employee_id):
    """
    Fetches the TODO list for a given employee ID from the API.
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    return response.json()


def main():
    """
    Main function to fetch and export the TODO list progress.
    """
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID")
        return

    employee_name = fetch_employee_name(employee_id)
    if not employee_name:
        print("No data found for employee ID {}".format(employee_id))
        return

    todos = fetch_employee_todo_list(employee_id)
    if not todos:
        print("No data found for employee ID {}".format(employee_id))
        return

    # Write to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = [
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ]
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
            quoting=csv.QUOTE_ALL
        )
        writer.writeheader()

        for todo in todos:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": todo['completed'],
                "TASK_TITLE": todo['title']
            })

    # Validate the number of tasks in the CSV
    total_tasks = len(todos)
    num_lines = 0
    with open(filename, 'r') as file:
        next(file)  # Skip header
        for line in file:
            if line.strip():  # Ignore empty lines
                num_lines += 1

    if total_tasks == num_lines:
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")


if __name__ == "__main__":
    main()
