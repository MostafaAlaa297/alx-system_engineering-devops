#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys


if __name__ == "__main__":
    ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    employeeURL = "{}/users/{}".format(url, ID)

    res = requests.get(employeeURL)

    todo_url = "{}/users/{}/todos".format(url, ID)

    res2 = requests.get(todo_url)

    completed = []

    for tasks in res2.json():
        if tasks.get("completed") is True:
            completed.append(tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        res.json().get("name"), len(completed), len(res2.json())))

    for task in completed:
        print("\t {}".format(task.get("title")))
