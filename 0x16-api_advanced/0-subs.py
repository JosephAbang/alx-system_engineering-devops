#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns int: The number of subscribers of the subreddit."""
    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {'User-Agent': 'Custom User Agent'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 400:
        return 0
    results = res.json().get("data")
    return results.get("subscribers")
