#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts on a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"
    headers = {'User-Agent': 'Custom User Agent'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        Print(None)
