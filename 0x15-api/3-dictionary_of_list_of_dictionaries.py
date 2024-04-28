#!/usr/bin/python3
'''
    script exports to-do list information of all employees to JSON format.
'''

import json
import requests


if __name__ == '__main__':

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todo.json()
    all_todo = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        all_todo[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_todo, f)
