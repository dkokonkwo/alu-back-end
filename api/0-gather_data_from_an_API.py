#!/usr/bin/python3
'''
function returns todo info an employee using id from API
'''


import requests
from sys import argv


def todo_progress(employee_id):
    '''get data from rest api'''
    base_url = "https://jsonplaceholder.typicode.com"
    todo_endpoint = "{}/todos".format(base_url)
    user_endpoint = "{}/users/{}".format(base_url, employee_id)

    try:
        user_response = requests.get(user_endpoint)
        user_response.raise_for_status()
        # above raises exception for unsuccessful request
        user = user_response.json()

        response = requests.get(todo_endpoint)
        todos = response.json()

        employee_name = user["name"]
        all_todos = [
            task for task in todos if task["userId"] == int(employee_id)
        ]
        completed_tasks = [todo for todo in all_todos if todo["completed"]]
        total_tasks = len(all_todos)
        total_completed = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, total_completed, total_tasks
        ))
        for each in all_todos:
            if each["completed"]:
                print("\t " + each["title"])

    except requests.exceptions.RequestException as e:
        print("An error occured: {}".format(e))

if __name__ == '__main__':
    id = argv[1]
    todo_progress(id)
