#!/usr/bin/env python


import sys
import json



sys.path.append('.')

scores = json.load(open('my_dictionary.txt'))


for tweet in sys.stdin:
    tweet_parsed = json.loads(tweet)
    if tweet_parsed['place'] != None:
        if (tweet_parsed['place'].get('country') == "United States" or tweet_parsed['place'].get(
                'country_code') == "US"):
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

                    if word.startswith('#'):
                        key = word
                        value = location
                    else:
                        key = location
                        value = str(score)

                    print('{0}\t{1}'.format(key, value))



# to test the reduce only


#with open('tweets.json', 'r') as file:
#    with open('reduce', 'w') as resuts:
#        tweets = file.read()[:-1]
#        tweets = tweets.split('\n')
#        for tweet in tweets:
#            tweet_parsed = json.loads(tweet)
#            if tweet_parsed['place'] != None:
#                if (tweet_parsed['place'].get('country') == "United States" or tweet_parsed['place'].get('country_code') == "US"):
#                    location = tweet_parsed['place'].get('full_name').split(',')
#                    if len(location) == 2:
#                        location = location[1].strip()
#                    if len(location) == 2:
#                        score = 0
#                        words = tweet_parsed['text'].split()
#                        for word in words:
#                            if word in scores:
#                                score += scores[word]
#                            else:
#                                score += 0
#
#                            if word.startswith('#'):
#                                key = word
#                                value = location
#                            else:
#                                key = location
#                                value = str(score)
#
#                            resuts.write('{0}\t{1}'.format(key, value) + '\n')
#                            print('{0}\t{1}'.format(key, value))
