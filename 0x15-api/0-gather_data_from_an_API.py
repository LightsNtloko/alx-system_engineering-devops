#!/usr/bin/python3
import sys
import requests

def fetch_employee_todo_list(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    return response.json()

def main():
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
    employee_name = f"Employee {employee_id}"  # Placeholder, replace with actual name if available
    
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"     {todo['title']}")

if __name__ == "__main__":
    main()
