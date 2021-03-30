# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:46:11 2021

@author: Max
"""
# Importing libraries for reqesting HTML and scraping the data
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Loading the worldmeters population table and its HTML
url = 'https://www.worldometers.info/world-population/'
page = requests.get(url)
#print(page)

# Parsing the HTML tags for the table
soup = BeautifulSoup(page.text, 'lxml')
#print(soup)


# Finding the HTML tags for the rows of data
table = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list' )
#print(table)

# Storing the table headers in a list
headers = []
for i in table.find_all('th'):
    headers.append(i.text)
    
# Putting all of the other data rows into a dataframe
df = pd.DataFrame(columns=headers)

for i in table.find_all('tr')[1:]:
    row = i.find_all('td')
    row_list = [j.text for j in row]
    df.loc[len(df)] = row_list

# Saving the table as a csv file
df.to_csv('C:/Users/Max/Desktop/web scraping course/table_scraped.csv')

