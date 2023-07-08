#!/usr/bin/python3
'''
function exports to json format todo 
info of all employees using id from API
'''


import json
import requests


def todo_progress():
    '''exports all employee info to json'''
    base_url = "https://jsonplaceholder.typicode.com"
    todo_endpoint = f"{base_url}/todos"
    users_endpoint = f"{base_url}/users"

    try:
        user_response = requests.get(users_endpoint)
        user_response.raise_for_status()
        # raises exception for unsuccessful request above
        users = user_response.json()

        response = requests.get(todo_endpoint)
        todos = response.json()

        all_todos = [task for task in todos]
        completed_tasks = [
            todo for todo in all_todos if todo["completed"]
        ]
        total_tasks = len(all_todos)
        total_completed = len(completed_tasks)

        # print(f"Employee {employee_name} 
        # is done with tasks({total_completed}/{total_tasks}):")
        # for each in all_todos:
        #     print("\t " + each["title"])

        # { "USER_ID": 
        # [ {"username": "USERNAME", "task": "TASK_TITLE", 
        #      "completed": TASK_COMPLETED_STATUS}, 
        #   {"username": "USERNAME", "task": "TASK_TITLE", 
        #      "completed": TASK_COMPLETED_STATUS}, ... ], 
        #   "USER_ID": 
        # [ {"username": "USERNAME", "task": "TASK_TITLE", 
        #     "completed": TASK_COMPLETED_STATUS}, 
        #   {"username": "USERNAME", "task": "TASK_TITLE", 
        #     "completed": TASK_COMPLETED_STATUS}, ... ]}

        data_2 = {}
        for user in users:
            list_tasks = []
            for todo in all_todos:
                task_dict = {}
                if user["id"] == todo["userId"]:
                    task_dict["username"] = user["username"]
                    task_dict["task"] = todo["title"]
                    task_dict["completed"] = todo["completed"]
                    list_tasks.append(task_dict)
            data_2[user['id']] = list_tasks

        # Export to JSON
        with open("todo_all_employees.json", "w") as json_file:
            json.dump(data_2, json_file, indent=4)

    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")

if __name__ == '__main__':
    todo_progress()
