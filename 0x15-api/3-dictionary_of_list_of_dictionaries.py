#!/usr/bin/python3
"""
Gather data from an API
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    employeeURL = "{}/users".format(url)

    filename = "todo_all_employees.json"

    res = requests.get(employeeURL)

    users = {}
    for user in res.json():
        users.update({user.get("id"): user.get("username")})

    data = {}
    for key, value in users.items():
        todo_url = "{}/users/{}/todos".format(url, key)
        res2 = requests.get(todo_url)

        all_tasks = []

        for task in res2.json():
            tasks = {
                    "username": value,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                    }
            all_tasks.append(tasks)

        data.update({key: all_tasks})

    with open(filename, "w") as json_file:
        json.dump(data, json_file)
