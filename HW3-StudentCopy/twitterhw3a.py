# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy

#my twitter account information


#boilerplate code for tweepy
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#update twitter status with media image with a status including the required hashtags
api.update_with_media('goldenretriever.jpg', status="#UMSI-206 #Proj3")
