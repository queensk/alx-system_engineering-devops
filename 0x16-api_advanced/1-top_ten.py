#!/usr/bin/python3
"""
Query the Reddit API and print the titles of the first 10 hot posts
"""


def top_ten(subreddit):
    """
    Gets top ten sub
    """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
