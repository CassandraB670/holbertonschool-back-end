#!/usr/bin/python3
"""Export data  in the CSV format"""

import csv
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    USER_ID = sys.argv[1]

    user_request = requests.get(f'{API_URL}/users/{USER_ID}').json()

    todo_list = requests.get(f"{API_URL}/todos?userId={USER_ID}").json()

    with open(f"{USER_ID}.csv", mode='w') as csv_file:
        writter = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            writter.writerow([
                user_request['id'],
                user_request['username'],
                task['completed'],
                task['title']
            ])

        print(f"Data as been exported to {USER_ID}.csv")
