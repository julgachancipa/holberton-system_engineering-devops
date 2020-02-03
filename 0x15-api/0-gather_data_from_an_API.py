#!/usr/bin/python3
"""9-starwars.py"""
import requests
import sys


if __name__ == "__main__":
    u = requests.get('https://jsonplaceholder.typicode.com/users/' +
                     sys.argv[1])
    t_d = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                       sys.argv[1])

    user_json = u.json()
    todos_json = t_d.json()

    todos_title = []
    completed = 0
    for todo in todos_json:
        todos_title.append(todo['title'])
        if todo['completed']:
            completed += 1

    print('Employee {} is done with tasks ({}/{}):'
          .format(user_json['name'], completed, len(todos_title)))
    for title in todos_title:
        print('\t ' + title)
