import tweepy
import nltk

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

public_tweets = api.search('UMSI')


adj_count = 0;

for tweet in public_tweets:
	print(tweet.text)
	tagged_tokens = nltk.pos_tag(tweet.text) # gives us a tagged list of tuples
	for (word, tag) in tagged_tokens:
		if tag == "JJ":
			adj_count+=1

print("There were ", adj_count,"adjectives in your tweets")
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

