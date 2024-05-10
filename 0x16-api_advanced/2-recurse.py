#!/usr/bin/python3
"""
Connect to Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recurse throw API"""
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
                url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    headers = {'User-Agent': 'Recurse'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])
    for post in posts:
        hot_list.append(post['data']['title'])

    after = data.get('data', {}).get('after')

    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
