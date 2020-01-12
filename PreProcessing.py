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

client = MongoClient()
client = MongoClient('localhost',27017)
db = client['MP-1']

posts = db.tweets
preprocessing = db.preprocessing

tweets = posts.find({})

userlist = []
retweetlist = []
outf = open('retweets.txt', 'w')
"""
for tweet in tweets:
	if tweet["screen_name"] not in userlist:
		userlist.append(tweet["screen_name"])

print userlist		

"""
def processHashtags(tweet):
	words = tweet["text"].split()
	#words = [u'RT', u'@iamvishalthakur:', u'\u092d\u0948\u092f\u093e', u'\u0915\u091f\u0915', u'\u092e\u0947\u0902', u'\u092a\u093e\u0928\u0940', u'\u0915\u0940', u'\u092c\u094b\u0924\u0932\u094b\u0902', u'\u0915\u0940', u'\u092c\u0930\u0938\u093e\u0924', u'\u0936\u0941\u0930\u0942', u'#IndvsSA']
	
	emoticon_regex = re.compile("(?:>?[:;=%8]'?[-o*,]?[()|\/0\]o\\D\[PpSs<>{}cOXx*])|(?:[()\\{}\/<\[>\]DOo0|SsXx*][-o*,]?'?[:=8;%]<?)|<3|\^\^|\^_\^|\\o\/|o\/")
	emoticonsInTweet = re.findall(emoticon_regex,tweet["text"])
	tweet["emoticons"] = emoticonsInTweet

	str = ""
	pylist = []
	#print type(tweet)
	#print tweet["text"]
	i=0
	#print "Words" , words
	#print len(words)
	
	while (i<len(words)):
		#print type(words[i])
		words[i] = words[i].encode('ascii','ignore')
		#print words[i]
		if(words[i]==''):
			i+=1
			continue
		#Removing the hash from the hashtags
		if(words[i][0] == '#'):
			words[i] = re.sub(r'#','',words[i])
			words[i] = re.sub(r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', '', words[i], flags=re.MULTILINE) #Removing the URLS
			words[i] = re.sub(r'\n', '', words[i], flags=re.MULTILINE) 	
			words[i] = re.sub(r'\|', '', words[i], flags=re.MULTILINE) 	
			words[i] = re.sub(r'&amp', '', words[i], flags=re.MULTILINE) 				
			words[i] = re.sub(r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', '', words[i], flags=re.MULTILINE) #Removing the URLS	
			#words[i] = re.sub(r'[;|:]', '', words[i], flags=re.MULTILINE) 							
			words[i] = re.sub(r'\\', '', words[i], flags=re.MULTILINE) #Removing the URLS	
			words[i] = re.sub(r'\\u[\w\d]*','',words[i])
			words[i] = re.sub(r'[.*]*','',words[i])
			pylist.append(words[i])
			#tweet["hashtags"] = tweet["hashtags"] + "," + words[i]
			tweet["hashtags"] = pylist

		else:
			if (words[i]=="RT"):
				i+=1
				continue

			if(words[i][0] == '@'):
				words[i] = re.sub(r'@','',words[i])
				words[i] = re.sub(r'[;|:|!|\"|,|)|?|.|\]|-]','', words[i], flags=re.MULTILINE)
				words[i] = re.sub(r'\'s', '', words[i], flags=re.MULTILINE)
				words[i] = re.sub(r'\'', '', words[i], flags=re.MULTILINE)
				words[i] = words[i].lower()

				if words[i] not in retweetlist:
					outf.write(words[i]+"\n")
					retweetlist.append(words[i])
					print words[i] 
				#print words[i]
				
							
			words[i] = re.sub(r'\n', '', words[i], flags=re.MULTILINE) 	
			words[i] = re.sub(r'\|', '', words[i], flags=re.MULTILINE) 	
			words[i] = re.sub(r'&amp', '', words[i], flags=re.MULTILINE) 				
			words[i] = re.sub(r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', '', words[i], flags=re.MULTILINE) #Removing the URLS	
			#words[i] = re.sub(r'[;|:]', '', words[i], flags=re.MULTILINE) 							
			words[i] = re.sub(r'\\', '', words[i], flags=re.MULTILINE) #Removing the URLS	
			words[i] = re.sub(r'\\u[\w\d]*','',words[i])
			#words[i] = re.sub(r'[.*]*','',words[i])
			words[i] = re.sub(emoticon_regex,'',words[i])
		#print "New Word" , words[i]

		str = str + words[i] + " "
		str.strip()
		tweet["text"] = str	
		i = i+1

		#print str

	del tweet["_id"]
	#print tweet
	preprocessing.insert_one(tweet).inserted_id	


		
for tweet in tweets:
	processHashtags(tweet)

outf.close()
#tweet = {}
