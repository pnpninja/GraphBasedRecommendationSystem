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

data = db.sample2_sportspersons
data1 = db.sample2_politicians
data2 = db.sample2_musicpersons
hierarchy = db.hierarchy
text_mining = db.text_mining
topics ={}
topics['sports'] = ['cricket','soccer','tennis','basketball','table tennis','hockey','chess','baseball','golf','rugby','chess']
topics['companies'] = ['computer','automotive','misc']
topics['music'] = ['MusicGroup','MusicalArtist']
topics['politics'] = ['India','US','UK','Pakistan','misc']
topics['technology'] = []
topics['vehicles'] = ['Airline','Car']
topics['media'] = ['Newspaper','Magazine','SocialMedia','Broadcaster']
locationList =[]
tweets = text_mining.find({})

count = 0
sportsCount = 0
politicsCount = 0
mediaCount = 0
vehiclesCount = 0
movieCount = 0
musicCount = 0
wordcount = 0

def f1():
    count =0
    sportsCount = 0
    politicsCount = 0
    mediaCount = 0
    vehiclesCount = 0
    movieCount = 0
    musicCount = 0
    wordcount = 0
    for tweet in tweets:
        #print "Here with " ,tweet['screen_name']
        wordcount=0
        count =0
        sportsCount = 0
        politicsCount = 0
        mediaCount = 0
        vehiclesCount = 0
        movieCount = 0
        musicCount = 0
        wordcount = 0
        for x in tweet['entities']:
            #print x

                wordcount+=1
                word = x["word"]
                if "Person" in x['dbpedia_types'] and len(x['dbpedia_types'])==1:
                    continue
                else:
                    if "Place" in x['dbpedia_types'] and "location" in x['freebase_types']:
                        if word not in locationList:
                            locationList.append(word)
                #            print word
                #            print locationList
                            count+=1

                        continue

                    #print word
                    search = hierarchy.find({"word":word})

                    for y in search:
                        #print "FOund", word
                        if "sports" in y['parentList']:
                            sportsCount+=1
                        if "music" in y['parentList']:
                            musicCount+=1
                        if "movies" in y['parentList']:
                            movieCount+=1
                        if "vehicles" in y['parentList']:
                            vehiclesCount+=1
                        if "media" in y['parentList']:
                            mediaCount+=1
                        if "politics" in y['parentList']:
                            politicsCount+=1

        try:
            sum =0
            sum+=sportsCount+movieCount+musicCount+politicsCount+vehiclesCount+mediaCount
            print "For" , tweet['screen_name']
            print "Sports Score " , sportsCount/float(wordcount)
            print "Music Score " , musicCount/float(wordcount)
            print "Movies Score " , movieCount/float(wordcount)
            print "POlitics Score " , politicsCount/float(wordcount)
            print "Vehicles Score " , vehiclesCount/float(wordcount)
            print "Media Score " , mediaCount/float(wordcount)

            print "Word count", wordcount

        except ZeroDivisionError as e:
                continue

        #print search

def f2():

    search = hierarchy.find()

    for text in search:
        if "politics" in text['parentList']:
            print text['word'], "->", text['parentList']

f1()