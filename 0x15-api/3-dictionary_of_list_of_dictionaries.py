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
