#!/usr/bin/python3
"""
    Fetches and displays TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.
"""


import json
import requests
import sys


if __name__ == '__main__':
    new_session = requests.Session()

    emp_id = sys.argv[1]
    id_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
    name_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"

    emp_todo = new_session.get(id_url)
    emp_name = new_session.get(name_url)

    json_res = emp_todo.json()
    name = emp_name.json()['name']

    total = 0

    for task_done in json_res:
        if task_done['completed']:
            total += 1

    print(f"Employee {name} is done with tasks({total}/{len(json_res)}):")
    for task_done in json_res:
        if task_done['completed']:
            print("\t " + task_done.get('title'))
