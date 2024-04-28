#!/usr/bin/python3
'''
    script exports to-do list information of all employees to JSON format.
'''

import json
import requests


if __name__ == '__main__':

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    all_todo = {}

    for user in users:
        tas_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                task_list.append(task_dict)
        all_todo[user.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_todo, f)
