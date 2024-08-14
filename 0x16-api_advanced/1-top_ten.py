#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'Linux:0x16.api.advanced:v1.0.0 (by u/lIGHTSnTLOKO'
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for i in range(min(10, len(posts))):
                print(posts[i]['data']['title'])
        except ValueError:
            print(None)
    else:
        print(None)
