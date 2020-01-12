import hashlib
import os
import threading
import time
import sys
import tweepy
import sys
import json
import argparse
import re
from nltk.corpus import stopwords
from pymongo import MongoClient
from collections import defaultdict
from collections import namedtuple

client = MongoClient()
client = MongoClient('localhost',27017)
db = client['MP-JJ']

posts = db.tweets
preprocessing = db.preprocessing

tweets = posts.find()
tweetscount = tweets.count()
tagOut = threading.Lock()
logLock = threading.Lock()
next_tweet_no = 0

def processFunction(tweet):
  print tweet["_id"]


class HashWorker (threading.Thread):
  def __init__(self, threadId):
    threading.Thread.__init__(self)
    self.threadId = threadId

  def run(self):
    global next_tweet_no

    logLock.acquire()
    print('Shift starting for worker %s' % self.threadId)
    logLock.release()
    working = True

    while working:
      tagOut.acquire()
      tweet = -1
      if next_tweet_no < tweetscount:
        tweet = tweets[next_tweet_no]
        next_tweet_no += 1
      tagOut.release()

      if tweet != -1:
        processFunction(tweet)
      else:
        working = False

    logLock.acquire()
    print('Worker %s ending shift' % self.threadId)
    logLock.release()


# Setup parameters of the work force
workForce = []
workerCount = 4


# Hire a workforce
for index in range(0,workerCount):
  worker = HashWorker(index)
  workForce.append(worker)

# Sign up the workers
for worker in workForce:
  worker.start()

# making sure they DO the job
for worker in workForce:
  worker.join()
