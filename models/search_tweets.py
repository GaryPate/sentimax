import tweepy
import time
from tweepy import OAuthHandler
import json
import os
import json
from datetime import datetime, timedelta

consumer_key = None
consumer_secret = None
access_token = None
access_secret = None

api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']
bearer_token = os.environ['BEARER_TOKEN']
access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']

# api_key = 'cqwHmCgGd6aF69MU0EThXnie3'
# api_secret = 'IbQiSyoK60nIwk5exc9NZDam3D0Ub0UiXiGsNKGpYf0FJWqddt'
# bearer_token = 'AAAAAAAAAAAAAAAAAAAAAOhuqgEAAAAAWiMzQ5eT02Gq3BFE0PwKR23f4P8%3DRprgve5QqT7W9kAL9qYme4FRk7VfNsiM3LDLerfawwKZ5C7jvx'
# access_token = '759628000044261376-8AB6F0Icz25tsYysVIdylyTRkmdve4I'
# access_secret = 'YQWtl4Z4LeaFUsy4VtUNHkH00leiHqeJHp9Uq8RhiJ32c'
# client_id = 'T2dtRGJDM2Z0QjM0Nmx3eTA5NWE6MTpjaQ'
# client_secret = 'fhWyswc4-m47GBp1AS-3MN7WK6q_ONF2bmryWFDXD3fT54e_7f'

auth = OAuthHandler(api_key, api_secret, access_token, access_secret)
# auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, timeout=90)

#streaming_client = tweepy.StreamingClient(bearer_token)
#samp = streaming_client.sample()

# ----------

client = tweepy.Client(bearer_token)

# Search Recent Tweets

# This endpoint/method returns Tweets from the last seven days


dt_end = datetime.now() - timedelta(hours=1)
dt_start = datetime.now() - timedelta(hours=2)
response = client.search_recent_tweets("Bitcoin")
qry = "Bitcoin"
tweets_ro = client.search_recent_tweets(query=qry
                                        , tweet_fields=['id','text','context_annotations','created_at','geo','author_id','lang','source']
                                        , expansions=["author_id", "geo.place_id"]
                                        , start_time = dt_start
                                        , end_time = dt_end
                                        , max_results=10
                                        )

tweets_data = tweets_ro.data

with open('tweet_data.json', 'w') as f:
    for tweet in tweets_data:
        print(tweet)
        f.write(json.dumps({'id': tweet.id, 'text': tweet.text}) + "\n")

# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields

# In this case, the data field of the Response returned is a list of Tweet
# objects
#tweets = response.data

# Each Tweet object has default ID and text fields
# for tweet in tweets_data:
#     print(tweet.id)
#     print(tweet.text)
#     print(tweet.meta)

# By default, this endpoint/method returns 10 results
# You can retrieve up to 100 Tweets by specifying max_results

#print(response)

# ----------

# with open('result.csv', 'a') as csvdump:
#     wTweet = csv.writer(csvdump, delimiter=';')

# class Listener(tweepy.Stream):
#     def on_status(self, status):
#         if status.lang == 'en':
#             print(status.text)
#             with open("UTWriter.txt", "a", encoding='utf-8') as writer:
#                 writer.write(status.text + "\n")



# while True:
#     try:
#         twitter_stream = streaming_client(auth, Listener())
#         twitter_stream.sample()

#     except IncompleteRead:
#         pass

#     except KeyboardInterrupt:
#         twitter_stream.disconnect()
#         break

# def record_data(input):
#     for line in input:
#         with open("record_data", "w") as log:
#             log.write(line)
