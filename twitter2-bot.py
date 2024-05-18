import tweepy

# Bearer token (for API v2)
bearer_token = "AAAAAAAAAAAAAAAAAAAAADlwtwEAAAAAB%2FQiKjzG20j6%2FU%2BoYujND4EQUDE%3DREIsoqa8qqMxbvZE9EE0mjJaE4Kmcgp7ELfflOxNrrqGHEoShN"

# Create a client object
client = tweepy.Client(bearer_token=bearer_token)

# The text of the tweet
tweet_text = "Hello from my Twitter bot!"

# Post the tweet
response = client.create_tweet(text=tweet_text)

print(f"Tweet ID: {response.data['id']}")
