#Forming sentences keeping the stop words and removing the hashtags and retweets.

import tweepy
import time
import os
import sys
import json
import argparse
import re,unicodedata
import nltk
from nltk.corpus import stopwords
from pymongo import MongoClient
from collections import defaultdict
from collections import namedtuple

client = MongoClient()
client = MongoClient('localhost',27017)
db = client['MP-1']

posts = db.preprocessing
stage1_tweets = db.stage1_tweets

tweets = posts.find()

# Populating the screen names with their usernames
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
		

def processTweets(tweet):

	text= tweet["text"].lower()
	stop = stopwords.words('english')
	description = tweet["description"].lower()
	pylist1=[]
	pylist2=[]
	str1 = ""
	str2 = ""
	for i in text.split():
			val=i
			if i in dict:
				val = dict[i]
			#pylist1.append(val)
			str1+=" " + val
			str1 = str1.strip(" ")
	print "TEXT" , str1		

	for i in description.split():
			val=i
			if i in dict:
				val = dict[i]
			pylist1.append(val)
			str2+=" " + val
			str2 = str2.strip(" ")

	print "DESCRIPTION" , str2

	tweet["text"] = str1
	tweet["description"] = str2
	#print tweet
	stage1_tweets.insert_one(tweet).inserted_id

for tweet in tweets:
	processTweets(tweet)			
