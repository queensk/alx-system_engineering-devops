#!/usr/bin/python3
"""
Get Reddit API
"""


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers
    """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    else:
        data = response.json()
        subscribers = data.get('data').get('subscribers')
    return subscribers
