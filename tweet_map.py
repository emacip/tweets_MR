#!/usr/bin/env python


import sys
import json



sys.path.append('.')

scores = json.load(open('my_dictionary.txt'))

"""Mapper Create key, value output to use in the reduce.

Usage::

    >>> read tweet.json
    >>> Reject tweets with place None or its not from US
    >>> Extract location 'TX'
    >>> Analyse words, if the word exist in the dictionary we use the score if not is 0, and save like key, value.
    >>> In case word is Hashtag, #Christmas saved like key and the state like value.

:param tweet: {"text": "Well damn.", "place": {"id": "1c69a67ad480e1b1", "url": "https://api.twitter.com/1.1/geo/id/1c69a67ad480e1b1.json", "place_type": "city", "name": "Houston", "full_name": "Houston, TX", "country_code": "US", "country": "United States", "bounding_box": {"type": "Polygon", "coordinates": [[[-95.823268, 29.522325], [-95.823268, 30.154665], [-95.069705, 30.154665], [-95.069705, 29.522325]]]}, "attributes": {}}}.
:output string: TX 5 OR #Christmas TX
"""
for tweet in sys.stdin:
    tweet_parsed = json.loads(tweet)
    count_tweets = 0
    if tweet_parsed['place'] != None:
        if (tweet_parsed['place'].get('country') == "United States" or tweet_parsed['place'].get('country_code') == "US"):
            location = tweet_parsed['place'].get('full_name').split(',')
            if len(location) == 2:
                location = location[1].strip()
            if len(location) == 2:
                count_tweets += 1
                words = tweet_parsed['text'].split()
                for word in words:
                    score = 0
                    if word in scores:
                        score += scores[word]
                    else:
                        score += 0

                    if word.startswith('#'):
                        key = word.encode('utf-8')
                        value = location
                    else:
                        key = location
                        value = score
                    print('{0}\t{1}'.format(str(key), str(value)))
                print('{0}\t{1}'.format("count_tweets", str(count_tweets)))
