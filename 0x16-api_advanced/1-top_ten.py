#!/usr/bin/python3
"""
Connect to Reddit API
"""
import requests


def top_ten(subreddit):
    """Get the top 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            children = data['data']['children']
            for post in children:
                print(post['data']['title'])
    else:
        print(None)
