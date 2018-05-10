Twitter_data.py:

Replace the value of str query (line 27) with the query you would like to search for. For example: "AAPL"(Apple), "TSLA"(Teslä), "BP(British Petroleum), etc.
replace the value of daymonth (line 30) with the date at which you would like to begin searchin from. For example, 311 is March 11. 
Line 35: the value in this while loop is the last date that you would like to search till. For example 307 is March 7. 
Run the file and it will automatically store all required data in CSV format.

tweets_polarity.py:
In lines 6,48, 78, and 109 replace the filename with the file that you would like to analyze. The program then does the rest by analyzing the 
polarity of the tweet and stores the total polarity for day and company in a CSV file. 

stock-data.ipynb:
This file will analyze and plot all of the stock data. After double checking to make sure that the file names correspond to your score files in cell 11, run all of the cells from the beginning. 

saveSentimentScores.ipynb: Analyzes every entry's (title + description) with Bluemix Natural Language Understadning and appends sentiment value to the data entry. Saves the new file in: filename_withScores.csv

augmentScores.ipynb: calculates the sentiment scores for every a list of news article

get_news_data.ipynb: gets news article data
