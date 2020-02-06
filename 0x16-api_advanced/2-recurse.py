#!/usr/bin/python3
"""list containing the titles of all hot articles"""
import requests
import sys


def recurse(subreddit, hot_list=[], next_pg=None):
    """all hot posts"""
    headers = {"User-Agent": "julgachancipa"}

    if next_pg:
        subRhot = requests.get('https://reddit.com/r/' + subreddit +
                               '/hot.json?after=' + next_pg,
                               headers=headers)
    else:
        subRhot = requests.get('https://reddit.com/r/' + subreddit +
                               '/hot.json', headers=headers)

    if subRhot.status_code == 404:
        return None

    subRhot_dict = subRhot.json()
    subRhot_data = subRhot_dict['data']
    next_pg = subRhot_data['after']
    subRhot_posts = subRhot_data['children']

    for post in subRhot_posts:
        post_data = post['data']
        hot_list.append(post_data['title'])

    if next_pg:
        recurse(subreddit, hot_list, next_pg)
    return hot_list
