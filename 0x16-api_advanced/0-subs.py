#!/usr/bin/python3

"""Queries Reddit API and returns the number of subscribers (not active user,
                                                             total subscribers)
for a given subreddit

Returns:
    0 if subreddit is invalid
"""
import requests


def number_of_subscribers(subreddit):
    """Queries reddit api for subscribers number in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "chukssomzzy-app/v0.0.1"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()["data"]
        return (data["subscribers"])
    else:
        return 0
