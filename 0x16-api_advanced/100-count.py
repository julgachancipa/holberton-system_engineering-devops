#!/usr/bin/python3
"""keywords titles of all hot articles"""
import requests
import sys


def count_words(subreddit, word_list, kw_cont={}, next_pg=None):
    """all hot posts by keyword"""
    headers = {"User-Agent": "julgachancipa"}

    if next_pg:
        subRhot = requests.get('https://reddit.com/r/' + subreddit +
                               '/hot.json?after=' + next_pg,
                               headers=headers)
    else:
        subRhot = requests.get('https://reddit.com/r/' + subreddit +
                               '/hot.json', headers=headers)

    if subRhot.status_code == 404:
        print()

    if kw_cont == {}:
        for word in word_list:
            kw_cont[word] = 0

    subRhot_dict = subRhot.json()
    subRhot_data = subRhot_dict['data']
    next_pg = subRhot_data['after']
    subRhot_posts = subRhot_data['children']

    for post in subRhot_posts:
        post_data = post['data']
        post_title = post_data['title']
        title_words = post_title.split()
        for w in title_words:
            for key in kw_cont:
                if w.lower() == key.lower():
                    kw_cont[key] += 1

    if next_pg:
        count_words(subreddit, word_list, kw_cont, next_pg)

    else:
        sorted_res = sorted(kw_cont.items(), reverse=True, key=lambda x: x[1])
        for res in sorted_res:
            if res[1] > 0:
                print('{}: {}'.format(res[0], res[1]))
