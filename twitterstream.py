import oauth2 as oauth
import urllib.request
import json
import re

# See Assignment 1 instructions or README for how to get these credentials
access_token_key = "165726561-iIzi7s5jXRT9pmQWsaNb7xoX0CaZgeydN2ykg9Cl"
access_token_secret = "5AVCNFZvSM6pSvb4iO5KILDXwdMSvu1nptlH4rlUw6ium"

consumer_key = "Idl031HytYZXJB2qY487zrnF2"
consumer_secret = "T26UQpyCRXgIeiSPlEwzB8SqGUeozkrI9OJ0RmJzUs6Zp5IUTf"

_debug = 0

oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler = urllib.request.HTTPHandler(debuglevel=_debug)
https_handler = urllib.request.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''


def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                                token=oauth_token,
                                                http_method=http_method,
                                                http_url=url,
                                                parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = urllib.request.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response


def fetchsamples():
    url = "https://stream.twitter.com/1.1/statuses/sample.json"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    with open('tweets_2.json', 'w') as my_tweets:
        for line in response:
            status = json.loads(line.decode('utf-8'))
            dict = {}
            if 'delete' not in status.keys():
                print(status)
                dict['text'] = status['text']
                dict['place'] = status['place']
                print("######")
                my_tweets.write(json.dumps(dict) + '\n')



if __name__ == '__main__':
    fetchsamples()
