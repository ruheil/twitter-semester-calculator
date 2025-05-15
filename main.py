import tweepy
from datetime import datetime
from backend import create_progress_bar, get_caption
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API credentials from environment variables
bearer = os.environ.get("BEARER_TOKEN")
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client(
    bearer_token=bearer,  
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    wait_on_rate_limit=True
)

# Create and post tweet
create_progress_bar()
media_id = api.media_upload(filename="progressbar.jpg").media_id_string
response = client.create_tweet(text=get_caption(), media_ids=[media_id], media_tagged_user_ids=[883790619818283008])
print(response)
