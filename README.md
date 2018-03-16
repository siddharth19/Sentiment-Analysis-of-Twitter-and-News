
# SENTIMENT ANALYSIS OF TWEETS AND NEWS

1. twitter_stream.py is used to get the tweets using the Twitter API (through python library tweepy) and store it in mongodb instance

2. Used  https://github.com/georgercooper/TwitterNER API for Named Entity Recognition from tweets
    NoisyNLP and run_ner.py is used
    Need to download http://nlp.stanford.edu/data/glove.twitter.27B.zip for this API

3.  news_stream.py is used to get the news from the News API (https://newsapi.org/) corresponding to the
    Named Entites

4. sentiment.py is used to perform the Sentiment Analysis and store it in the .csv files.
    TextBlob is used to perform the Sentiment Analysis

5. plot.py is used to plot the graph b/w sentiment and count corresponding to each named entity

6. plot2.py is used to plot the graph b/w time and sentiment value corresponding to each named entity.

7. The sentiments corresponding to the tweets of the named entities are stored in the .csv file.

8. Data Folder contains the mongodb files

## Named Entites from the data are:

1. Trump
2. Miami
3. Russia
4. Twitter
5. God

1st graph for entity "Trump":

!

2nd graph for entity "Trump":

!

