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


#boilerplate code for tweepy
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#search for public tweets matching search term
public_tweets = api.search("noDAPL")

total_tweets = 0
total_tweet_polarity = 0
total_tweet_subjectivity = 0

#for loop to iterate through each tweet matching search term
for tweet in public_tweets:
	#increment total tweet count
	total_tweets += 1
	#print each tweet
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	#add each tweet's polarity into total polarity
	total_tweet_polarity += analysis.sentiment[0]
	#add each tweet's subjectivity into total subjectivity
	total_tweet_subjectivity += analysis.sentiment[1]

#print total tweets, must convert to a string first
print ("Total number of tweets is " + str(total_tweets))

#print average subjectivity, divide total_tweet_subjectivity by total tweet count, then convert to string
print ("Average subjectivity is " + str(total_tweet_subjectivity/total_tweets))

#print average polarity, divide total_tweet_polarity by total tweet count, then convert to string
print ("Average polarity is " + str(total_tweet_polarity/total_tweets))

