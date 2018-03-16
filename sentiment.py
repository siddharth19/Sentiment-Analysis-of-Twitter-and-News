from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from pprint import pprint
from pymongo import MongoClient
from textblob import TextBlob
from run_ner import TwitterNER
from twokenize import tokenizeRawTweetText
from newsapi import NewsApiClient
from httplib import IncompleteRead
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json
import re
import operator

count = 10000

connection = MongoClient("mongodb://localhost")

def clean(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+) | ([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", text).split())

def getSentiment(text = ""):
    blob = TextBlob(clean(text))
    return blob.sentiment.polarity

def getSentValue(s = 0):
    if s > 0:
        return 1
    elif s < 0:
        return -1
    elif s == 0.0:
        return 0

db = connection.tweets

fp = open("tweets_key1.csv", "w")
fp.write("Setiment_Value,Sentiment,Time\n")
collection = db['tweet_key1']
cursor = collection.find({})
for tweet in cursor:
    text = tweet['text']
    created = tweet['created']
    s = getSentiment(text)
    sv = getSentValue(s)
    fp.write("%s, %s, %s\n" % (str(s), str(sv), created))

fp = open("tweets_key2.csv", "w")
fp.write("Setiment_Value,Sentiment,Time\n")
collection = db['tweet_key2']
cursor = collection.find({})
for tweet in cursor:
    text = tweet['text']
    created = tweet['created']
    s = getSentiment(text)
    sv = getSentValue(s)
    fp.write("%s, %s, %s\n" % (str(s), str(sv), created))

fp = open("tweets_key3.csv", "w")
fp.write("Setiment_Value,Sentiment,Time\n")
collection = db['tweet_key3']
cursor = collection.find({})
for tweet in cursor:
    text = tweet['text']
    created = tweet['created']
    s = getSentiment(text)
    sv = getSentValue(s)
    fp.write("%s, %s, %s\n" % (str(s), str(sv), created))

fp = open("tweets_key4.csv", "w")
fp.write("Setiment_Value,Sentiment,Time\n")
collection = db['tweet_key4']
cursor = collection.find({})
for tweet in cursor:
    text = tweet['text']
    created = tweet['created']
    s = getSentiment(text)
    sv = getSentValue(s)
    fp.write("%s, %s, %s\n" % (str(s), str(sv), created))

fp = open("tweets_key5.csv", "w")
fp.write("Setiment_Value,Sentiment,Time\n")
collection = db['tweet_key5']
cursor = collection.find({})
for tweet in cursor:
    text = tweet['text']
    created = tweet['created']
    s = getSentiment(text)
    sv = getSentValue(s)
    fp.write("%s, %s, %s\n" % (str(s), str(sv), created))

db = connection.news

fp = open("news_key1.csv", "w")
fp.write("Setiment_Value,Sentiment,Time\n")
collection = db['news_key1']
cursor = collection.find({})
for news in cursor:
    text = news['news']
    created = news['created']
    s = getSentiment(text)
    sv = getSentValue(s)
    fp.write("%s, %s, %s\n" % (str(s), str(sv), created))

fp = open("news_key2.csv", "w")
fp.write("Setiment_Value,Sentiment,Time\n")
collection = db['news_key2']
cursor = collection.find({})
for news in cursor:
    text = news['news']
    created = news['created']
    s = getSentiment(text)
    sv = getSentValue(s)
    fp.write("%s, %s, %s\n" % (str(s), str(sv), created))

fp = open("news_key3.csv", "w")
fp.write("Setiment_Value,Sentiment,Time\n")
collection = db['news_key3']
cursor = collection.find({})
for news in cursor:
    text = news['news']
    created = news['created']
    s = getSentiment(text)
    sv = getSentValue(s)
    fp.write("%s, %s, %s\n" % (str(s), str(sv), created))

fp = open("news_key4.csv", "w")
fp.write("Setiment_Value,Sentiment,Time\n")
collection = db['news_key4']
cursor = collection.find({})
for news in cursor:
    text = news['news']
    created = news['created']
    s = getSentiment(text)
    sv = getSentValue(s)
    fp.write("%s, %s, %s\n" % (str(s), str(sv), created))

fp = open("news_key5.csv", "w")
fp.write("Setiment_Value,Sentiment,Time\n")
collection = db['news_key5']
cursor = collection.find({})
for news in cursor:
    text = news['news']
    created = news['created']
    s = getSentiment(text)
    sv = getSentValue(s)
    fp.write("%s, %s, %s\n" % (str(s), str(sv), created))

pprint("Hello")

