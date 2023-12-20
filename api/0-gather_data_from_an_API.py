#!/usr/bin/python3
"""Script using REST API for returns information about TODO list
usin REST API"""

import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    user_query = requests.get(f'{API_URL}/users/{sys.argv[1]}')
    user_data = user_query.json()

    todo_list_query = requests.get(f'{API_URL}/todos?userID={sys.argv[1]}')
    todo_list = todo_list_query.json()

    finished_tasks = [task for task in todo_list if task['completed']]

    user_name = user_data['name']
    len_finished_tasks = len(finished_tasks)
    todo = len(todo_list)

    print("Employee {} is done with tasks({}/{}):".format(
        user_name,
        len_finished_tasks,
        todo))

    for task in finished_tasks:
        print(f"\t {task['title']}")
