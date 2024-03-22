import tweepy
# API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
client_id = ''
client_secret = ''
# Authenticate with Twitter API
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

client.create_tweet(text='tweet')
