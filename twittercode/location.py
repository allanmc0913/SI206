import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "3006509597-dSfovhqgakdhl5YzjPr62n2LhW8VET3iDuI4x4q"
access_token_secret = "3mnJDMPA8DEM6roaEjfJ3yNAYYKhlp1oPdOsXuujKjNwI"
consumer_key = "pLUjmsAzgYqU4e3799AdHtfGG"
consumer_secret = "pQqFUfpulRaGo4BiAT3chpw1jaBT3HFE6i2mppcFFiEWCuYn4O"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('"Gilmore Girls" geocode:40.6781784,-73.94415789999999,10km')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data
