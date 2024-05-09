#!/usr/bin/python3
"""Queries the Reddit API and
    returns the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Returns:
        int: The number of subscribers of the subreddit. 
        Returns 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data['data']['subscribers']
    elif res.status_code == 302:
        return 0
    else:
        return 0
