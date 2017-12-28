import tweepy
import credentials
import helper

class TwitterStreamListener(tweepy.StreamListener):

    def __init__(self, api=None):
        super(TwitterStreamListener, self).__init__()  
        print ("Strem Initialized ...")

    def on_status(self, status):
        #print(helper.cleanTweet(status))
        cleaned = helper.cleanTweet(status)
        positive, negative, neutral, polarity = helper.getSentiments(helper.getTweetText(status))
        # send positive, negative, neutral to live feed
        #save to csv
        print("Writing tweet to csv...")
        helper.saveToCSV(status, polarity)
        print("Writing done...")
        print("Result : ", polarity)


    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False