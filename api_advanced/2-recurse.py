#!/usr/bin/python3
"""Recursively collect the titles of all hot posts of a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles, or None if invalid."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0"}
    response = requests.get(url, headers=headers,
                            params={"after": after, "limit": 100},
                            allow_redirects=False)
    if response.status_code != 200:
        return None if after is None else hot_list
    data = response.json().get("data", {})
    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
