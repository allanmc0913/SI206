# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

access_token = "3006509597-dSfovhqgakdhl5YzjPr62n2LhW8VET3iDuI4x4q"
access_token_secret = "3mnJDMPA8DEM6roaEjfJ3yNAYYKhlp1oPdOsXuujKjNwI"
consumer_key = "pLUjmsAzgYqU4e3799AdHtfGG"
consumer_secret = "pQqFUfpulRaGo4BiAT3chpw1jaBT3HFE6i2mppcFFiEWCuYn4O"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search("noDAPL")

total_tweets = 0
tweet_pol = 0
tweet_sub = 0
for tweet in public_tweets:
	total_tweets += 1
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	tweet_pol += analysis.sentiment[0]
	tweet_sub += analysis.sentiment[1]

print ("Total number of tweets is " + str(total_tweets))
print ("Average subjectivity is " + str(total_tweets/tweet_pol))
print ("Average polarity is " + str(total_tweets/tweet_sub))

