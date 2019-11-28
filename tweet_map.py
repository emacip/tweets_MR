#!/usr/bin/env python

import sys
import json

sys.path.append('.')

scores = json.load(open('my_dictionary.txt'))


with open('tweets_2.json', 'r') as file:
    tweets = file.read()[:-1]
    tweets = tweets.split('\n')
    for tweet in tweets:
        tweet_parsed = json.loads(tweet)
        if tweet_parsed['place'] != None:
            if (tweet_parsed['place'].get('country') == "United States" or tweet_parsed['place'].get('country_code') == "US"):
                location = tweet_parsed['place'].get('full_name').split(',')
                if len(location) == 2:
                    location = location[1].strip()

                if len(location) == 2:
                    score = 0
                    words = tweet_parsed['text'].split()
                    for word in words:
                        if word in scores:
                            score += scores[word]
                        else:
                            score += 0
                        print('{0}\t{1}'.format(location, score))

