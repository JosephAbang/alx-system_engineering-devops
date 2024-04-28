#!/usr/bin/python3
"""
    Records all tasks that are owned by this employee
    Export data in the JSON format
"""


import csv
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
    _user = emp_name.json()['username']

    total = []
    updateUser = {}
    for _all in json_res:
        total.append(
                {
                    "task": _all.get('title'),
                    "completed": _all.get('completed'),
                    "username": _user,
                })
    updateUser[emp_id] = total
    json_file = emp_id + '.json'
    with open(json_file, 'w') as f:
        json.dump(updateUser, f)
