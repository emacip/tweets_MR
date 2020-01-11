#!/usr/bin/env python

import sys

"""Reduce Create key, value results output.

Usage::

    >>> read map output
    >>> If key is a Hashtag, saved in the hashtag dictionary
    >>> If key is a word, saved in the dic dictionary with the metadata total words analyse, score happines, total words for mean
    >>> Generate output Happines Score , Total Words , Words Mean from the dic dictionary
    >>> Generate output Hashtags order by number of Hashtags 

:param string: TX 5
:output string: TX	Happines Score : 2 Total Tweets: 9  Mean : 1
"""

dic = {}
hashtag = {}
tweets = {}
tweets["count_tweets"] = 0

for line in sys.stdin:
    key, value = line.split('\t')
    if key.startswith('#'):
        if key not in hashtag:
            hashtag[key] = 1
        else:
            hashtag[key] += 1
    elif key == "count_tweets":
        tweets["count_tweets"] += int(value)
    else:
        value = int(value)

        if key not in dic:
            dic[key] = {}
            dic[key]['total'] = {}
            dic[key]['score'] = {}
            dic[key]['total_mean'] = {}
            dic[key]['total'] = 1
            if value != 0:
                dic[key]['total_mean'] = 1
            else:
                dic[key]['total_mean'] = 0
            dic[key]['score'] = value
        else:
            dic[key]['total'] += 1
            if value != 0:
                dic[key]['total_mean'] += 1
            dic[key]['score'] += value

for key in dic.keys():
    if dic[key]['total_mean'] == 0:
        mean = 0
    else:
        mean = dic[key]['score'] / dic[key]['total_mean']

    print('{0}\t{1}'.format(key, "Happines Score : " + str(dic[key]['score']) + " Total Words: " + str(
        dic[key]['total']) +" Total Words Value : "+ str(dic[key]['total_mean']) + "  Words Mean : " + str(mean)))

"""Order dictionary Hashtag base in count values"""
aux = {k: v for k, v in sorted(hashtag.items(), reverse=True, key=lambda item: item[1])[:10]}

for key in aux.keys():
    print('{0}\t{1}'.format(key, hashtag[key]))

print('{0}\t{1}'.format("count_tweets", tweets["count_tweets"]))
