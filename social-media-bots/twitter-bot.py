import tweepy

# API keys
consumer_key = "MXGEeX0cs0h67Lmjz51lZ48m1"
consumer_secret = "aUSuXlqXjv5BQvnAv8gVrlHTFL8jwGGyGS9CDREtXfWOeuTZ3z"
access_token = "716726492298878976-C39xSu2xHwblyqhcFDxBLOgLlJRHN8T"
access_token_secret = "KCfG1MT3e0E0RaEP2gBpM8ZrbLykIU8gDwZIiFLVQfRXi"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
tweet = "Hello from my Twitter bot!"
api.update_status(tweet)
