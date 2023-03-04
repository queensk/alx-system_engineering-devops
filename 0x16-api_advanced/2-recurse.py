#!/usr/bin/python3
"""
Reddit API to query the hot articles for a given subreddit
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Recursive function that queries the Reddit API
    """
    import requests
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyBot/0.0.1"}
    response = requests.get(
        url,
        params={
            "count": count,
            "after": after},
        headers=headers,
        allow_redirects=False)

    if response.status_code >= 400:
        return None

    data = response.json()["data"]
    if not data["children"]:
        return hot_list
    for article in data["children"]:
        hot_list.append(article["data"]["title"])

    recurse(subreddit, hot_list, data["after"])
