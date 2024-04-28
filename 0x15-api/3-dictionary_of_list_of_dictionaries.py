#!/usr/bin/python3
'''
    script exports to-do list information of all employees to JSON format.
'''

import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    _users = requests.get(url + 'users').json()
    with open('todo_all_employees.json', 'w+') as json_f:
        json.dump({
            j.get('id'): [{
                'task': i.get('title'),
                'completed': i.get('completed'),
                'username': j.get('username')
            } for i in requests.get(url + 'todos',
                                    params={'userId': j.get('id')}).json()]
            for j in _users}, json_f)
