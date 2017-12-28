import helper
import pandas as pd


class OldStats(object):
    
    def __init__(self):
        print("OldStats Initialized ...")
    
    def getStats(self):
        '''
            Do shit here 
        '''
        self.oldData = helper.readCsv(helper.getFileUri())
        #oldStats = self.cleanData()
        self.Stats = []
        for index, row in self.cleanData():
            st_group = row.groupby(['sentiment'])
            s = []
            #fname = helper.getAirlineName(index)
            senti = {}
            for i, row in st_group:
                senti[str(i)] = row.shape[0] 
                
            s.append(senti)
            s.append(str(index))
            self.Stats.append(s)
        return self.Stats
        print("return Stats")

    def cleanData(self):
        df = self.oldData
        del df['id']
        del df['tweetedby']
        del df['text']
        del df['tweet_id']
        del df['tweet_location']
        g1 = df.groupby(df["airline"])
        oldStats = df.groupby(['airline'])
        return oldStats