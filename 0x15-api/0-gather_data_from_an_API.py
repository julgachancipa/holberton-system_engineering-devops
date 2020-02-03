#!/usr/bin/python3
"""user todos"""
import requests
import sys


if __name__ == "__main__":
    u = requests.get('https://jsonplaceholder.typicode.com/users/' +
                     sys.argv[1])
    t_d = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                       sys.argv[1])

    user_json = u.json()
    todos_json = t_d.json()

    done_title = []
    completed = 0
    all_t = 0
    for todo in todos_json:
        if todo['completed']:
            completed += 1
            done_title.append(todo['title'])
        all_t += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(user_json['name'], completed, all_t))
    for title in done_title:
        print('\t ' + title)
