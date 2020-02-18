#!/usr/bin/python3
"""number of subscribers for a given subreddit"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Return number of subscribers"""
    headers = {"User-Agent": "julgachancipa"}

    subRinfo = requests.get('https://reddit.com/r/' + subreddit +
                            '/about.json', headers=headers)

    if subRinfo.status_code == 404:
        return 0
    subRinfo_dict = subRinfo.json()
    subRinfo_data = subRinfo_dict['data']
    return (subRinfo_data['subscribers'])
