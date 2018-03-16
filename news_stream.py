from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from pprint import pprint
from pymongo import MongoClient
from textblob import TextBlob
from run_ner import TwitterNER
from twokenize import tokenizeRawTweetText
from newsapi import NewsApiClient

import json
import re
import operator

count = 10000

ner = TwitterNER()

def ner_tweet(tweet):
    global ner
    l = []
    print(tweet)
    tokens = tokenizeRawTweetText(tweet)
    list = ner.get_entities(tokens)
    print(list)
    for x in list:
        l.append(str(" ".join(tokens[int(x[0]):int(x[1])]).encode('utf-8')))
    return l

dict={}

connection = MongoClient("mongodb://localhost")
db = connection.tweets
collection = db['tweets']
cursor = collection.find({})

for tweet in cursor:
    text = tweet['text']
    #print((ner_tweet(text)))
    tw = ner_tweet(text)
    for x in tw:
        if x in dict:
            dict[x] += 1
        elif x.lower() in dict:
            dict[x.lower()] += 1
        elif x.upper() in dict:
            dict[x.upper()] += 1
        else:
            dict[x] = 1

stw = sorted(dict.items(), key=operator.itemgetter(1))
stw = stw[::-1]

i = 0
key = []

for x in stw:
    i += 1
    key.append(x[0])
    if i >= 20:
        break

print(key)

def insert_news(news):
    print("Hello")
    n = 1
    l = []
    articles = news['articles']
    for x in articles:
        head = x['title']
        news_sno = n
        timestamp = x['publishedAt']
        n += 1
        news_head = {'sno': news_sno, 'news': head, 'created': timestamp}
        l.append(news_head)
    return l

db = connection.news
newsapi = NewsApiClient(api_key='54fc5717f29942ada37bc72e28e335fb')

i=0
j = 0
key1 = []
l=[]
while l==[]:
    top_headlines = newsapi.get_top_headlines(q=key[i], language='en')
    l = insert_news(top_headlines)
    i += 1
key1.append(key[i-1])
db.news_key1.insert_many(l)

l=[]
while l==[]:
    top_headlines = newsapi.get_top_headlines(q=key[i], language='en')
    l = insert_news(top_headlines)
    i += 1
key1.append(key[i-1])
db.news_key2.insert_many(l)

l=[]
while l==[]:
    top_headlines = newsapi.get_top_headlines(q=key[i], language='en')
    l = insert_news(top_headlines)
    i += 1
key1.append(key[i-1])
db.news_key3.insert_many(l)

l=[]
while l==[]:
    top_headlines = newsapi.get_top_headlines(q=key[i], language='en')
    l = insert_news(top_headlines)
    i += 1
key1.append(key[i-1])
db.news_key4.insert_many(l)

l=[]
while l==[]:
    top_headlines = newsapi.get_top_headlines(q=key[i], language='en')
    l = insert_news(top_headlines)
    i += 1
key1.append(key[i-1])
db.news_key5.insert_many(l)

db = connection.tweets
collection = db['tweets']
cursor = collection.find({})
t = 1
j = 1
k = 1
l = 1
m = 1

for tweet in cursor:
    text = tweet['text']
    tw = ner_tweet(text)
    if key1[0] in tw:
        tweet["sno"] = t
        t += 1
        db.tweet_key1.insert_one(tweet)
    if key1[1] in tw:
        tweet["sno"] = j
        j += 1
        db.tweet_key2.insert_one(tweet)
    if key1[2] in tw:
        tweet["sno"] = k
        k += 1
        db.tweet_key3.insert_one(tweet)
    if key1[3] in tw:
        tweet["sno"] = l
        l += l
        db.tweet_key4.insert_one(tweet)
    if key1[4] in tw:
        tweet["sno"] = m
        m += 1
        db.tweet_key5.insert_one(tweet)

pprint("Hello")

