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
clean_tweets = db.clean_tweets

tweets = posts.find()

usernames = []

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


def removestopwords(tweet):
	text= tweet["text"].lower()
	stop = stopwords.words('english')
	description = tweet["description"].lower()
	pylist1=[]
	pylist2=[]
	#pylist1 = [i for i in text.split() if i not in stop]
	for i in text.split():
		val=i
		if i not in stop:
			if i in dict:
				val = dict[i]
			pylist1.append(val)
	#pylist2 = [i for i in description.split() if i not in stop]

	for i in description.split():
		val=i
		if i not in stop:
			if i in dict:
				val = dict[i]
			pylist2.append(val)

	del tweet["_id"]
	tweet["text"] = pylist1
	tweet["description"] = pylist2
	#print tweet
	clean_tweets.insert_one(tweet).inserted_id


for tweet in tweets:
	removestopwords(tweet)


