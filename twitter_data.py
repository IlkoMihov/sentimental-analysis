# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 11:31:52 2018

@author: yumen
"""

import json
import oauth2 as oauth
import pandas as pd




def data_to_df(filename):
    file = open(filename, "r")
    pd.DataFrame.from_csv(file)

def get_data():
    consumer_key = "H9OKRfMqEBib1x5Qgg01Nn9u6"
    consumer_secret = "x4MkUYBPEVu1KnVGqy0JImrq29f929xuVFEQFMyeMmUJBivqVU"
    access_token = "975761944962650112-HpzmKcjD5IZ2Zb82cqCKnCEAMURR0lF"
    access_token_secret = "l9JbivssGKANtQExneLDMByj9vHGYUrwkNHvDBHR9VpQz"
    URL = "https://api.twitter.com/1.1/search/tweets.json?q=AAPL:\)&result_type=popular&count=100&tweet_mode=extended"
    
    consumer = oauth.Consumer(key=consumer_key, secret = consumer_secret)
    access_token = oauth.Token(key = access_token, secret = access_token_secret)
    client = oauth.Client(consumer, access_token)
    response, data = client.request(URL)
    file = open("Apple_tweets.csv", "w")
    # extracting data in json format and writing it to CSV file
    for tweet in json.loads(data)['statuses']:
        try:
            ''' 
            file.write(tweet['full_text'])
            file.write(",")
            file.write(tweet["retweet_count"])
            file.write(",")
            file.write(tweet["favorite_count"])
            file.write(",1")
            '''
            #print(tweet["full_text"], tweet["retweet_count"], tweet["favorite_count"])
            info = "\"" + tweet['full_text'] + "\"" + "," + tweet["retweet_count"] + "," + tweet["favorite_count"] + "1"
            #info = ",".join([str("\"" + tweet['full_text'] + "\""),tweet["retweet_count"] ,tweet["favorite_count"] , "1"])            
            print(info)
            file.write(info)
            file.write("\n")
        except Exception: 
            pass
    URLnegative = "https://api.twitter.com/1.1/search/tweets.json?q=AAPL:\(&result_type=popular&count=100&tweet_mode=extended"
    response, data = client.request(URLnegative)
    # extracting data in json format and writing it to CSV file 
    for tweet in json.loads(data)['statuses']:
        try:
            #print(tweet["retweet_count"])
            info =  "\"" + tweet['full_text']+ "\"" + "," + tweet["retweet_count"] + "," + tweet["favorite_count"] + ",1"
            print(info)
            file.write(info)
            file.write("\n")    
        except Exception:
            pass
    file.close()
    
get_data()
#data_to_df("Apple_tweets.csv")
