#!/usr/bin/python3
"""
    Records all tasks that are owned by this employee
    format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
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

    total = 0

    for task_done in json_res:
        if task_done['completed']:
            total += 1

    csv_file = emp_id + '.csv'
    _user = emp_name.json()['username']

    with open(csv_file, "w", newline='') as file:
        write = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in json_res:
            write.writerow([emp_id, _user, i.get('completed'), i.get('title')])
