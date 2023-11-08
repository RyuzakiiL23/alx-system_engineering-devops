#!/usr/bin/python3
"""Query that returns the 10 hot titles"""
import requests


def top_ten(subreddit):
    """Function that returns the 10 hot titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, headers=None, params={"limit": 10},
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")
    hot_10 = [(x.get("data").get("title")) for x in results.get("children")]
    for hot in hot_10:
        print(hot)
