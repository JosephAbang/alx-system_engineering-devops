#!/usr/bin/python3
'''
    script exports to-do list information of all employees to JSON format.
'''

import json
import requests


if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    _todo = todo.json()
    todoAll = {}

    for user in users:
        taskList = []
        for task in _todo:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
