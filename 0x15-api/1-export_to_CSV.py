#!/usr/bin/python3
"""export to csv"""
import csv
import requests
import sys


if __name__ == "__main__":
    u = requests.get('https://jsonplaceholder.typicode.com/users/' +
                     sys.argv[1])
    t_d = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                       sys.argv[1])

    user_json = u.json()
    todos_json = t_d.json()

    file_name = sys.argv[1] + '.csv'
    with open(file_name, 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos_json:
            data = [todo['userId'], user_json['username'],
                    todo['completed'], todo['title']]
            writer.writerow(data)
