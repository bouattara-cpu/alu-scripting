#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu_scripting:v1.0 (by /u/TON_PSEUDO)"}
    try:
        response = requests.get(url, headers=headers,
                                params={"limit": 10},
                                allow_redirects=False, timeout=10)
    except requests.RequestException:
        print(None)
        return
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
