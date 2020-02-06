#!/usr/bin/python3
"""titles of the first 10 hot posts listed"""
import requests
import sys


def top_ten(subreddit):
    headers = {"User-Agent": "julgachancipa"}

    subRhot = requests.get('https://reddit.com/r/' + subreddit +
                           '/hot.json?sort=hot&limit=10', headers=headers)

    subRhot_dict = subRhot.json()
    subRhot_data = subRhot_dict['data']
    subRhot_posts = subRhot_data['children']

    if len(subRhot_posts) == 0:
        print(None)
        return

    for post in subRhot_posts:
        post_data = post['data']
        print(post_data['title'])
