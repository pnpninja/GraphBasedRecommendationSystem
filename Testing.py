#File to do random tests
import tweepy
import time
import os
import sys
import json
import argparse
import re,unicodedata
from pymongo import MongoClient
from collections import defaultdict
from collections import namedtuple

"""
CONSUMER_KEY = "dMTZrL3z7EXmcJWpRlfDGTT8w"
CONSUMER_SECRET = "3Hf0eFs31qhpMEp1QmUY4fIV5E5BERuYIDN0LBfElS8xHOnc3e"
ACCESS_TOKEN = "2998218985-0g8Z7LcLRLINNwBLE4ROoNyYKAmdtpE2bIfLOET"
ACCESS_TOKEN_SECRET = "kl2Hr6Ii2w0GWFgVPbx23UsSNbBJtwDWpjGCOELuKJNsc"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

try:
	status = api.get_user(screen_name='iamyouvraj')
	json_data = str(json.dumps(status._json))
	json_string = json.loads(json_data)
	print json_string["name"]

except tweepy.TweepError as e:
	if e.message[0]['code'] == 34:
		print "YESs"
	print e.message[0]['message']

"""

dict={}

inf = open('usernames.txt','r')
count = 1
key = ""
for line in inf:
	if count%2==1:
		key = line.strip("\n")
		count+=1
	else:
		value = line.strip("\n")
		if value=='':
			value = "Random"

		dict[key] = value
		count+=1

#print dict
print dict['_oodell']
print dict['nanditathhakur']