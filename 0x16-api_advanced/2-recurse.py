#!/usr/bin/python3
"""
Make use of reddit's API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """recursively returning top ten post titles"""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    parameters = {'after': after}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, params=parameters,
                            headers=user_agent, allow_redirects=False)
    if response.status_code != 200:
        return (None)
    else:
        after_data = response.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = response.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
