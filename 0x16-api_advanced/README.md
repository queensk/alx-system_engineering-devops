# 0x16. API advanced

## Description

This project focuses on making recursive requests to an API, how to use an API with pagination and how to read API documentation to find the endpoints we’re looking for.

## Background Context

Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

## Table of contents

| Files                          | Description                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [0-subs.py](./0-subs.py)       | Python function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit |
| [1-top_ten.py](./1-top_ten.py) | Python function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit                      |
| [2-recurse.py](./2-recurse.py) | Python recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit      |
