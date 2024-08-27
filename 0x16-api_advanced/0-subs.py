#!/usr/bin/python3
"""API user reddit to print out the nubmer of subscribers of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribers in a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User.agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)


    if response.status_code != 200:
        return 0


    data = response.json().get("data")
    num_subs = data.get("subscribers")


    return num_subs
