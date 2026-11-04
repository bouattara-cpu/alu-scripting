#!/usr/bin/python3
"""Recursively count keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in hot post titles."""
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0"}
    response = requests.get(url, headers=headers,
                            params={"after": after, "limit": 100},
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for word in title.lower().split():
            counts[word] = counts.get(word, 0) + 1
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    lowered = [w.lower() for w in word_list]
    totals = {}
    for word in set(lowered):
        total = counts.get(word, 0) * lowered.count(word)
        if total > 0:
            totals[word] = total
    for word, total in sorted(totals.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, total))
