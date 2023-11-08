#!/usr/bin/python3
"""Query that returns the number hot titles"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursive function that returns the number hot titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "MyRedditBot:v1.0.0"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for x in results.get("children"):
        hot_list.append(x.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
