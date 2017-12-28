import streamListener
import helper
import old_stats
import credentials

from tweepy import OAuthHandler 
from tweepy import Stream

if __name__ == '__main__':
    TwitterStreamListner = streamListener.TwitterStreamListener()
    access_token, access_token_secret, consumer_key, consumer_secret = credentials.getCredentials()
    auth = OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    stream = Stream(auth, TwitterStreamListner)
    stream.filter(track=helper.getHandlesToTrack(), async=False)
