#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles, and prints a sorted
"""


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Count words
    """
    import requests

    # Base case: no more articles to query
    if after == "":
        # Sort counts by descending value and then by ascending key
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        # Print the counts in the desired format
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return

    # Query the Reddit API
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(
            f"Error {response.status_code}: Could not query subreddit {subreddit}")
        return

    # Parse the titles of the articles and count the keywords
    data = response.json()
    articles = data["data"]["children"]
    for article in articles:
        title = article["data"]["title"]
        for word in word_list:
            if word.lower() in title.lower().split():
                if word.lower() in counts:
                    counts[word.lower()] += 1
                else:
                    counts[word.lower()] = 1

    # Recursively call the function with the next page of articles
    next_after = data["data"]["after"]
    count_words(subreddit, word_list, next_after, counts)
