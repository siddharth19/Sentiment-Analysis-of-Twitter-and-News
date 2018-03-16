from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from pprint import pprint
from pymongo import MongoClient
import json

ACCESS_TOKEN = '------------------------'
ACCESS_SECRET = '-----------------------'
CONSUMER_KEY = '------------------------'
CONSUMER_SECRET = '-------------------------'

class TweetListener(StreamListener):
    
    def __init__(self, count=0, i=0):
        self.count = count
        self.n = 1
        self.i = i
    
    def on_data(self, data):
        t = json.loads(data)
        pprint(t)
        tweet_sno = (self.i) * 10 + self.n
        tweet_id = t['id_str']
        text = t['text']
        hashtags = t['entities']['hashtags']
        time_stamp = t['created_at']
        tweet = {'sno': tweet_sno, 'id': tweet_id, 'text': text, 'hashtags': hashtags, 'created': time_stamp}
        db.tweets.insert_one(tweet)
        self.n += 1
        self.count -= 1
        if self.count <= 0:
            return False
        else:
            return True
    
    def on_error(self, status):
        print status

count = 100
connection = MongoClient("mongodb://localhost")
db = connection.tweets

for i in range(100):
    l = TweetListener(count, i)
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    stream = Stream(auth, l)
    tweets = stream.sample(languages=["en"])

