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

CONSUMER_KEY = "dMTZrL3z7EXmcJWpRlfDGTT8w"
CONSUMER_SECRET = "3Hf0eFs31qhpMEp1QmUY4fIV5E5BERuYIDN0LBfElS8xHOnc3e"
ACCESS_TOKEN = "2998218985-0g8Z7LcLRLINNwBLE4ROoNyYKAmdtpE2bIfLOET"
ACCESS_TOKEN_SECRET = "kl2Hr6Ii2w0GWFgVPbx23UsSNbBJtwDWpjGCOELuKJNsc"

CONSUMER_KEY1 = "wDUMiq14AOwemQkp2o76GNDFY"
CONSUMER_SECRET1 = "2AR2PCYGpmmvAg3yea42AV2OdFvYO4F0ccJlLuefmPOetuy0uq"
ACCESS_TOKEN1 = "2922548846-y5q0kyTn2NUJYQPVwDqsXpYIahYLTOq99A7DCi5"
ACCESS_TOKEN_SECRET1 = "DPLw8ckDWKMokRrJZHqIfw2bShChRqInKQhoCQlkXYkAy"

CONSUMER_KEY2 = "1xJfc4v50qPy7oEdxaPiie4Yk"
CONSUMER_SECRET2 = "BEKneYP05dRLfGLu6HpsNN6qF6HVJI2TVouORJTwDQZPg7LZ5S"
ACCESS_TOKEN2 = "2998218985-ug3BPNQPcQuAzHRAYUzWQhUvPfwUXDbOGxMLaeN"
ACCESS_TOKEN_SECRET2 = "TJCpnNZjYquX8O5Lm3TdqfTb33ntEEWHAXyaqYUc6AiQo"

CONSUMER_KEY3 = "lGjocYLMXWZcDs4kzJC8jExQw"
CONSUMER_SECRET3 = "rLPDldUClmzY7vgvFbscGKwWMAguCqMovMdfGDeDzu3EI5D03B"
ACCESS_TOKEN3 = "2998218985-LjTKBeaS7ksadZuzmyFh1kkG5bSKgUVYSeDS9yy"
ACCESS_TOKEN_SECRET3 = "MQgZcvtN5ucpObwEm3DXJwfR60OFCslgGq7UZamcqtGJN"

CONSUMER_KEY4 = "lJOJc0aky4zLSuEo6eJFVC3Eh"
CONSUMER_SECRET4 = "bmLV1JzgqqAexqWKUTdf9e52WuvW1etVDzrolPubBhozlgBXA4"
ACCESS_TOKEN4 = "2998218985-Su826b2Yw3D7t3MlwGgNCxU1QlSsrgh59yrK66z"
ACCESS_TOKEN_SECRET4 = "nnAGYLGQrjwnIOY75u24qixbsGoDGbYpEfh7b1euQGkt7"

CONSUMER_KEY5 = "uZ2zywhtZo5RqEmmnJe9cLfQB"
CONSUMER_SECRET5 = "iOJka2mZQDOPFaLl5gOFQbsuvAm60gyu2DIqO2cyG6o4GXcyP0"
ACCESS_TOKEN5 = "2922548846-sNsn1QXIvWsXi99dDLpMZrjW3nKVzwjrjbN6DMH"
ACCESS_TOKEN_SECRET5 = "KnLhU8yEuAn2eMn2qabtDER7ArHdwoItFaO8O5tRhZamM"

CONSUMER_KEY6 = "mHVQipkGWSF7MU0BwdoZ4eBO2"
CONSUMER_SECRET6 = "qkrGKa6e1BGHxdjcJ8H0DT9UIrSnHlSpAu3jHCUdW5TosdRB0v"
ACCESS_TOKEN6 = "2922548846-d0vbBB7T3FT6wnU3PXPehrmSC1F0YPlESk8hJ5m"
ACCESS_TOKEN_SECRET6 = "hjEqYIPpWnQGdhiW1Wd5PzxOdFEEmTQE89ANbd9MnDeB9"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

auth = tweepy.OAuthHandler(CONSUMER_KEY1, CONSUMER_SECRET1)
auth.set_access_token(ACCESS_TOKEN1, ACCESS_TOKEN_SECRET1)
api1 = tweepy.API(auth)

auth = tweepy.OAuthHandler(CONSUMER_KEY2, CONSUMER_SECRET2)
auth.set_access_token(ACCESS_TOKEN2, ACCESS_TOKEN_SECRET2)
api2 = tweepy.API(auth)

auth = tweepy.OAuthHandler(CONSUMER_KEY3, CONSUMER_SECRET3)
auth.set_access_token(ACCESS_TOKEN3, ACCESS_TOKEN_SECRET3)
api3 = tweepy.API(auth)

auth = tweepy.OAuthHandler(CONSUMER_KEY4, CONSUMER_SECRET4)
auth.set_access_token(ACCESS_TOKEN4, ACCESS_TOKEN_SECRET4)
api4 = tweepy.API(auth)

auth = tweepy.OAuthHandler(CONSUMER_KEY5, CONSUMER_SECRET5)
auth.set_access_token(ACCESS_TOKEN5, ACCESS_TOKEN_SECRET5)
api5 = tweepy.API(auth)

auth = tweepy.OAuthHandler(CONSUMER_KEY6, CONSUMER_SECRET6)
auth.set_access_token(ACCESS_TOKEN6, ACCESS_TOKEN_SECRET6)
api6 = tweepy.API(auth)

count = 0

retweetlist=[]
outf = open('usernames.txt', 'a')
inf = open('retweets.txt', 'r')
logf = open('logs.txt', 'a')
#try:
for line in inf:	
	
	try:
		print line
		if (count%7)==0:
			print "Calling API-1"
			status = api.get_user(screen_name=line)
			count+=1

		elif (count%7)==1:
			print "Calling API-2"
			status = api1.get_user(screen_name=line)
			count+=1

		elif (count%7)==2:
			print "Calling API-3"
			status = api2.get_user(screen_name=line)
			count+=1

		elif (count%7)==3:
			print "Calling API-4"
			status = api3.get_user(screen_name=line)
			count+=1

		elif (count%7)==4:
			print "Calling API-5"
			status = api4.get_user(screen_name=line)
			count+=1

		elif (count%7)==5:
			print "Calling API-6"
			status = api5.get_user(screen_name=line)
			count+=1

		elif (count%7)==6:
			print "Calling API-7"
			status = api6.get_user(screen_name=line)
			count+=1

		json_data = str(json.dumps(status._json))
		json_string = json.loads(json_data)
		outf.write(line)
		name = json_string["name"].encode('ascii','ignore').strip()
		outf.write(name)
		outf.write("\n")

	except tweepy.TweepError as e:
		if e.message[0]['code'] == 34:
			logf.write(line)
			count+=1
			continue
		elif e.message[0]['code'] == 88:
			print "Exceeded"
			break
	#print e.message[0]['message']
			
inf.close()
outf.close()
logf.close()