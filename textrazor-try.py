import textrazor
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

stage1_tweets = db.stage1_tweets
tweets = stage1_tweets.find({"screen_name":"henrywinter"})

textrazor.api_key = "cef16432f0181fea21a77289db5194626939595e3292ab4e610028a7"
client = textrazor.TextRazor(extractors=["entities", "topics"])
outf = open('analysis.txt','w')

def categorize(tweet):
	response = client.analyze(tweet["text"])
	for entity in response.entities():
		print entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types
		outf.write(str(entity.id) + "\n" + str(entity.relevance_score) + "\n" + str(entity.confidence_score) + "\n" + str(entity.freebase_types) + "\n")
		print type(entity.id), type(entity.relevance_score), type(entity.confidence_score), type(entity.freebase_types)

count = 1
for tweet in tweets:
	 categorize(tweet)
