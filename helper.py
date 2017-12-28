from textblob import TextBlob
import pandas as pd
import re
import json
import csv

# Data File Uri
fileURI = 'data/AS.csv'

def getSentiments(tweet):
    '''
    '''
    
    analysis = TextBlob(removeNoiseFromText(tweet))
    # set sentiment
    positive = -1
    negative = -1
    neutral = -1
    if analysis.sentiment.polarity > 0:
        positive = (analysis.sentiment.polarity)*100
    elif analysis.sentiment.polarity == 0:
        neutral = (analysis.sentiment.polarity)*100
    else:
        negative = (analysis.sentiment.polarity)*100
    return positive, negative, neutral, getPolarity(analysis)
    


def cleanTweet(tweet):
    '''
    clean tweet text by removing links, special characters
    '''
    return tweet._json

def getTweetText(tweet):
    return tweet.text

def readCsv(uri):
    return pd.read_csv(uri,encoding = "ISO-8859-1")

def getHandlesToTrack():
    return ['@united', '@geekwhocodes','@shaillyrathore1','@VirginAmerica','@SouthwestAir','@Delta','@USAirways','@AmericanAir']

def removeNoiseFromText(text, char='@'):
    filter(lambda x:x[0]!=char, text.split())
    return " ".join(filter(lambda x:x[0]!=char, text.split()))

def saveToCSV(status, polarity):
    id = status.id
    sentiment = polarity
    airline = getAirlineNumber(status.entities['user_mentions'][0]['name'])
    tweetedby = status.user.name
    text = status.text
    tweet_id = id
    tweet_location = status.user.location
    with open(fileURI, 'a', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        data = [[id, sentiment,airline, tweetedby, text, tweet_id, tweet_location]]
        a.writerows(data)
    

def getPolarity(analysis):
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1


def getFileUri():
    return fileURI

def getAirlineNumber(airline):
    r = 0
    if(airline is 'Virgin America'):
        return 1
    elif (airline is 'United'):
        return 2
    elif (airline is 'Southwest'):
        return 3
    elif (airline is 'Delta'):
        return 4
    elif (airline is 'US Airways'):
        return 5
    elif (airline is 'American'):
        return 6
    else:
        return 0

def getAirlineName(num):
    r = 0
    if(num == 1 ):
        return 'Virgin America'
    elif (num == 2):
        return 'United'
    elif (num == 3 ):
        return 'Southwest'
    elif (num == 4):
        return 'Delta'
    elif (num == 5):
        return 'US Airways'
    elif (num == 6 ):
        return 'American'
    else:
        return 'None'