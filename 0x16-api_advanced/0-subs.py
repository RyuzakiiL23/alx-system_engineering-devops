#!/usr/bin/python3
"""Query that returns the number of redit subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Function that returns the number of redit subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=None, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    return data.get("subscribers")
