# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

#my twitter account information
access_token = "3006509597-dSfovhqgakdhl5YzjPr62n2LhW8VET3iDuI4x4q"
access_token_secret = "3mnJDMPA8DEM6roaEjfJ3yNAYYKhlp1oPdOsXuujKjNwI"
consumer_key = "pLUjmsAzgYqU4e3799AdHtfGG"
consumer_secret = "pQqFUfpulRaGo4BiAT3chpw1jaBT3HFE6i2mppcFFiEWCuYn4O"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#search for public tweets matching 
public_tweets = api.search("noDAPL")


total_tweets = 0
total_tweet_polarity = 0
total_tweet_subjectivity = 0

#for loop to iterate through each tweet matching search term
for tweet in public_tweets:
	#increment total tweet count
	total_tweets += 1
	#print tweet
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	#add each tweet's polarity into total polarity
	total_tweet_polarity += analysis.sentiment[0]
	#add each tweet's subjectivity into total subjectivity
	total_tweet_subjectivity += analysis.sentiment[1]

#print total tweets, must convert to a string first
print ("Total number of tweets is " + str(total_tweets))

#print average subjectivity, divide tweet_sub by total tweet count, then convert to string
print ("Average subjectivity is " + str(tweet_subjectivity/total_tweets))

#print average polarity, divide tweet_pol by total tweet count, then convert to string
print ("Average polarity is " + str(tweet_polarity/total_tweets))

