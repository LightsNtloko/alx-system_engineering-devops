import json
import requests

# Fetch user data
users_url = "https://jsonplaceholder.typicode.com/users"
users_response = requests.get(users_url)
users = users_response.json()

# Fetch task data
tasks_url = "https://jsonplaceholder.typicode.com/todos"
tasks_response = requests.get(tasks_url)
tasks = tasks_response.json()

# Organize the data
todo_data = {}

for user in users:
    user_id = user["id"]
    username = user["username"]
    user_tasks = [
        {
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        }
        for task in tasks if task["userId"] == user_id
    ]
    todo_data[user_id] = user_tasks

# Export data to JSON file
with open("todo_all_employees.json", "w") as json_file:
    json.dump(todo_data, json_file)

print("Data exported to todo_all_employees.json")
