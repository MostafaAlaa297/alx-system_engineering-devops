#!/usr/bin/python3
"""
Gather data from an API
"""
import json
import requests
import sys


if __name__ == "__main__":
    ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    employeeURL = "{}/users/{}".format(url, ID)

    res = requests.get(employeeURL)

    todo_url = "{}/users/{}/todos".format(url, ID)

    res2 = requests.get(todo_url)

    filename = "{}.json".format(ID)
    username = res.json().get("username")

    all_tasks = []

    for task in res2.json():
        tasks = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
                }
        all_tasks.append(tasks)

    data = {ID: all_tasks}

    with open(filename, "w", newline="") as json_file:
        json.dump(data, json_file)
