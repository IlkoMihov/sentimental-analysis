# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 11:31:52 2018

@author: yumen
"""

import json
import requests as r 
''' 
from textblob import TextBlob
import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize
print(sent_tokenize(example_sentence))  # Split text by sentence ( may be usefull to get rid of useless information in tweets)
print(workd_tokenize(example_sentence))  #Split sentence by words

''' 


def get_data():
    bearer_token_encoded = "czhXUVdFT1RKckRPUG9xckFURkRPdFFMWDpkMDJYbExBdlZoaG10dzNSQVYySEh3eGZSZk9BemNHdW4zY2JnUWd4eGdhbng0TklJeA=="
    
    URL = "https://api.twitter.com/1.1/tweets/search/fullarchive/SentimentalAnalysis.json"
    file = open("tweets_30day_Tesla.csv" , "a")
    tokenURL = "https://api.twitter.com/oauth2/token"
    b_token = r.post(tokenURL, headers = {"Authorization" : "Basic " + str(bearer_token_encoded), "Content-type":"application/x-www-form-urlencoded;charset=UTF-8"},  data = {"grant_type":"client_credentials"})
    token = b_token.json()["access_token"]
    header ={"Authorization": "Bearer "+token} 
    query = "TSLA"
    daymonth = 311
    date = "20180" + str(daymonth)+ "0000"
    toDate = "20180" + str(daymonth)+ "2359"
    params = {"query":query, "fromDate":date, "toDate":toDate} 
    #file.write("tweet,date\n")
    while daymonth>=307:
        # extracting data in json format and writing it to CSV file
        data = r.post(URL, data = json.dumps(params), headers = header)
        data = data.json()
        #writing first page to file
        for tweet in data["results"]:
            try:
                extended_tweet = tweet["extended_tweet"]
                text = extended_tweet["full_text"]
                text = text.replace(",", " ")
                date = tweet["created_at"]
                info = "\"" + text+ "\"," + date +"\n"
                file.write(info)
                print(info)
            except Exception: 
                pass
        file.write("\n")
        ''' 
        #Writing the second page 
        try: #Sometimes there is no second page. 
            nextPage = data["next"] 
            params["next"] = nextPage
            data = r.post(URL, data = json.dumps(params), headers = header)
            data = data.json()
            print("\n\n\nNow page 2:\n\n")
            for tweet in data["results"]:
                try:
                    extended_tweet = tweet["extended_tweet"]
                    text = extended_tweet["full_text"]
                    text = text.replace(",", " ")
                    date = tweet["created_at"]
                    info = "\"" + text+ "\"," + date +"\n"
                    file.write(info)
                    print(info)
                except Exception: 
                    pass
        except Exception:
            pass
        ''' 
        daymonth = daymonth-1
        date = "20180" + str(daymonth)+ "0000"
        toDate = "20180" + str(daymonth)+ "2359"
        params = {"query":query, "fromDate":date, "toDate":toDate} 
    file.close()
get_data()
