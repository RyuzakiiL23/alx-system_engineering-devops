#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Query that returns the number of redit subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        "User-Agent": "MyRedditBot:v1.0.0"
    }
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
