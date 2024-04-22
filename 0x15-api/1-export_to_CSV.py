#!/usr/bin/python3
"""
Gather data from an API
"""
import csv
import requests
import sys


if __name__ == "__main__":
    ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    employeeURL = "{}/users/{}".format(url, ID)

    res = requests.get(employeeURL)

    todo_url = "{}/users/{}/todos".format(url, ID)

    res2 = requests.get(todo_url)

    filename = "{}.csv".format(ID)
    username = res.json().get("username")

    with open(filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in res2.json():
            comp = task.get("completed")
            title = str(task.get("title"))
            writer.writerow([ID, username, comp, title])
