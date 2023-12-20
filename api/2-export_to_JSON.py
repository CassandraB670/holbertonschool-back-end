#!/usr/bin/python3
"""Export data  in the JSON format"""

import json
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':

    USER_ID = sys.argv[1]

    user_request = requests.get(f'{API_URL}/users/{USER_ID}').json()

    todo_list = requests.get(f"{API_URL}/todos?userId={USER_ID}").json()

    json_filename = f"{USER_ID}.json"

    data = {
        USER_ID: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_request['username']
            }
            for task in todo_list
        ]
    }

    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file)
