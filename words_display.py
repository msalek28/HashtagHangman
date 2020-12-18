#imports the tweepy module to access twitter information and time
import tweepy
import time

#enters my key and secret to access tweepy's tools
consumer_key = "my_user_key"
consumer_secret = "my_secret_user_key"

#authorizes my use of tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

#pulls the trends for philadelphia
data = api.trends_place(2471217)

#pulls out all of the hashtags in the trends
hashtags = [trend['name'] for trend in data[0]['trends'] if trend['name'].startswith('#')]

#removes the hashtags from the words
words = [word.replace('#', '') for word in hashtags]

#generates a capitalized list of the trending hashtags
word_list = [x.upper() for x in words]

