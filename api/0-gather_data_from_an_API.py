#!/usr/bin/python3
'''
function returns todo info an employee using id from API
'''

from sys import argv
import requests

def todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    todo_endpoint = f"{base_url}/todos"
    user_endpoint = f"{base_url}/users/{employee_id}"

    try:
        user_response = requests.get(user_endpoint)
        user_response.raise_for_status() # raises exception for unsuccessful request
        user = user_response.json()
        
        response = requests.get(todo_endpoint)
        todos = response.json()

        employee_name = user["name"]
        all_todos = [task for task in todos if task["userId"] == int(employee_id)]
        completed_tasks = [todo for todo in all_todos if todo["completed"]]
        total_tasks = len(all_todos)
        total_completed = len(completed_tasks)

        print(f"Employee {employee_name} is done with tasks({total_completed}/{total_tasks}):")
        for each in all_todos:
            print("\t " + each["title"])

    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")



if __name__ == '__main__':
    id = argv[1]
    todo_progress(id)