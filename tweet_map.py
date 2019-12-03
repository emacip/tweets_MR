#!/usr/bin/env python


import sys
import json
import urllib2



sys.path.append('.')

# My public dictionary in S3 to use in EMR
content = urllib2.urlopen('https://emb-pract-hadoop.s3-eu-west-1.amazonaws.com/my_dictionary.txt')
scores = json.load(content)


for tweet in sys.stdin:
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



# to test the reduce only

#with open('tweets_4.json', 'r') as file:
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
#                            resuts.write('{0}\t{1}'.format(location, score) + '\n')
#                            print('{0}\t{1}'.format(location, score))