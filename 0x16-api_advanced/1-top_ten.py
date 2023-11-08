#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """Query that returns the number of redit subscribers"""
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
