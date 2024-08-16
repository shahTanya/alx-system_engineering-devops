#!/usr/bin/python3
"""Get the top 10 post in a reddit"""

import requests


def top_ten(subreddit):
    """Gets the 10 top post"""
    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit=10"
    headers = {"User-Agent": "chukssomzzy-app/v0.0.1"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        top_ten_posts = r.json()["data"]
        for top_post in top_ten_posts["children"]:
            print(top_post["data"]["title"])
    else:
        print(None
