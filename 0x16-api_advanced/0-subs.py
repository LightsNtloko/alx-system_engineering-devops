#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 '
            'Safari/537.36'
        )
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 404:
            return 0

        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)

        return 0
    except requests.RequestException:
        return 0
