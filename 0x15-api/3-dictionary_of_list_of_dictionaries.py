#!/usr/bin/python3
"""export to json"""
import json
import requests
import sys


if __name__ == "__main__":
    us = requests.get('https://jsonplaceholder.typicode.com/users/')

    users_dict = us.json()

    data = {}

    for user in users_dict:
        t_d = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId=' +
            str(user['id']))
        todos_list = t_d.json()
        data_list = []
        for to_do in todos_list:
            task_d = {}
            task_d['task'] = to_do['title']
            task_d['completed'] = to_do['completed']
            task_d['username'] = user['username']
            data_list.append(task_d)
        data[user['id']] = data_list

    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as jsonfile:
        json.dump(data, jsonfile)
