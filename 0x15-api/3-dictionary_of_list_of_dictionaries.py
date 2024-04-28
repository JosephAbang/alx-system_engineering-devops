#!/usr/bin/python3
'''
    script exports to-do list information of all employees to JSON format.
'''

import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    _users = requests.get(url + 'users').json()
    all_employees_data = {}

    for user in _users:
        user_id = user.get('id')
        user_todos = requests.get(url + 'todos',
                                        params={'userId': user_id}).json()
        user_tasks = [{'task': todo.get('title'),
                    'completed': todo.get('completed'),
                    'username': user.get('username')}
                for todo in user_todos]
        all_employees_data[user_id] = user_tasks

    with open('todo_all_employees.json', 'w+') as json_f:
        json.dump(all_employees_data, json_f)
