# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 12:55:39 2018

@author: yumen
"""
import csv
from textblob import TextBlob
#Title + Description
file = csv.reader(open("tweets_30day_Apple.csv", "r"), delimeter = ",") #file with scores
file_polarity = open("tweets_30day_polarity.csv", "w")  #file we write results to
polarity_per_day = {}       #stores the sum of polarities for every date
count_per_day = {}  #counts entries per day
total = count = 0   #pretty sure this is not used 
for line in file.readlines():
    string = ""
    string += line
    if "," in line:
        ''' 
        Next two lines were used to obtain the date from my CSV File. 
        This will be different for yours 
        '''
        tweet, date = string.split(",") 
        date = date[3:10]
        
        
        if ";" not in date:               #Used to remove some faulty entries 
            tweetBlob = TextBlob(tweet) #Create Textblob
            polarity = tweetBlob.sentiment.polarity #Get polarity
            if date in polarity_per_day.keys(): #Enter into dictionary
                polarity_per_day[date] +=polarity
                count_per_day[date] +=1
            else:
                polarity_per_day[date] = polarity
                count_per_day[date] = 1
            string = ""
file_polarity.write("Company,")
for key in count_per_day.keys(): #Write keys to csv(Header)
    string= key+","
    file_polarity.write(string)
file_polarity.write("\nApple,")
for key in polarity_per_day.keys(): #Write polarities to CSV
    daily = polarity_per_day[key]/count_per_day[key]
    print(key, ": ", daily)
    string = str(daily) + ","
    file_polarity.write(string)

'''

file_polarity.write("\nTesla,")
file = open("tweets_30day_Tesla.csv", "r")
polarity_per_day = {}
count_per_day = {}
for line in file.readlines():
    string = ""
    string += line
    if "," in line:
        tweet, date = string.split(",")
        date = date[3:10]
        if ";" not in date:                
            tweetBlob = TextBlob(tweet)
            polarity = tweetBlob.sentiment.polarity
            if date in polarity_per_day.keys():
                polarity_per_day[date] +=polarity
                count_per_day[date] +=1
            else:
                polarity_per_day[date] = polarity
                count_per_day[date] = 1
            string = ""
print("Tesla")
for key in polarity_per_day.keys():
    daily = polarity_per_day[key]/count_per_day[key]
    print(key, ": ", daily)
    string = str(daily) + ","
    file_polarity.write(string)
file_polarity.write("\nGoldman Sachs,")
file = open("tweets_30day_GoldmanSachs.csv", "r")
polarity_per_day = {}
count_per_day = {}
total = count = 0 
for line in file.readlines():
    string = ""
    string += line
    if "," in line:
        tweet, date = string.split(",")
        date = date[3:10]
        if ";" not in date:                
            tweetBlob = TextBlob(tweet)
            polarity = tweetBlob.sentiment.polarity
            if date in polarity_per_day.keys():
                polarity_per_day[date] +=polarity
                count_per_day[date] +=1
            else:
                polarity_per_day[date] = polarity
                count_per_day[date] = 1
            string = ""
print("Goldman Sachs")
for key in polarity_per_day.keys():
    daily = polarity_per_day[key]/count_per_day[key]
    print(key, ": ", daily)
    string = str(daily) + ","
    file_polarity.write(string)
file_polarity.write("\nBritish Petroleum,")
file = open("tweets_30day_BritishPetroleum.csv", "r")
polarity_per_day = {}
count_per_day = {}
total = count = 0 
for line in file.readlines():
    string = ""
    string += line
    if "," in line:
        tweet, date = string.split(",")
        date = date[3:10]
        if ";" not in date:                
            tweetBlob = TextBlob(tweet)
            polarity = tweetBlob.sentiment.polarity
            if date in polarity_per_day.keys():
                polarity_per_day[date] +=polarity
                count_per_day[date] +=1
            else:
                polarity_per_day[date] = polarity
                count_per_day[date] = 1
            string = ""
print("British Petroleum")
for key in polarity_per_day.keys():
    daily = polarity_per_day[key]/count_per_day[key]
    print(key, ": ", daily)
    string = str(daily) + ","
    file_polarity.write(string)    
'''
file_polarity.close()
