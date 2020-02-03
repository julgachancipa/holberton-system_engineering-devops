#!/usr/bin/python3
"""export to json"""
import json
import requests
import sys


if __name__ == "__main__":
    u = requests.get('https://jsonplaceholder.typicode.com/users/' +
                     sys.argv[1])
    t_d = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                       sys.argv[1])

    user_json = u.json()
    todos_list = t_d.json()

    data_list = []
    for to_do in todos_list:
        task_d = {}
        task_d['task'] = to_do['title']
        task_d['completed'] = to_do['completed']
        task_d['username'] = user_json['username']
        data_list.append(task_d)

    data = {}
    data[sys.argv[1]] = data_list

    file_name = sys.argv[1] + '.json'
    with open(file_name, 'w') as jsonfile:
        json.dump(data, jsonfile)
