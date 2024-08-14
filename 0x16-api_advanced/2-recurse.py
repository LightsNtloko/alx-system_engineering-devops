#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'Linux:0x16.api.advanced:v2.22.o (by u/lIGHTSnTLOKO)'
    }
    params = {'after': after} if after else {}

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            articles = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after')
            
            if articles:
                hot_list.extend(article['data']['title'] for article in articles)
            
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list

        except ValueError:
            return None

    return None
