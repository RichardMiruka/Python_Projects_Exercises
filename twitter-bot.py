import tweepy

# API keys
consumer_key = "ikqQJ2mik9F5EWVLODRM5Gyn6"
consumer_secret = "HACUeZ0N03prPuDacMJCHlkdiN3GOJ96R2EVzMK8BxZrsww8er"
access_token = "716726492298878976-zVELgE4ff1UstkRhADgtDYQOyNKfhR2"
access_token_secret = "IrdF32HTguJdxHP5AYmIu0FK4aINThE9zctR0VHHtfzRF"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
tweet = "Hello from my Twitter bot!"
api.update_status(tweet)
