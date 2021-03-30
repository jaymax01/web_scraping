# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:27:27 2021

@author: Max
"""
# Importing libraries for requesting HTML and scraping data
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Loading the carpages listings website and dataframe to hold the dataset
url = 'https://www.carpages.ca/used-cars/search/?num_results=50&fueltype_id%5b0%5d=3&fueltype_id%5b1%5d=7&p=1'
page = requests.get(url)
#print(page)

soup = BeautifulSoup(page.text, 'lxml')
#print(soup)

df = pd.DataFrame({'Link':[''], 'Name':[''], 'Price':[''], 'Color':[''], 'Description':['']})

# Collecting information from the boards to store in the dataframe

counter = 0

while counter < 10:
    
    postings = soup.find_all('div', class_ = 'media soft push-none rule')
    #print(postings)
    
    try:
        
     
        for post in postings:        
           landing_page = post.find('a', class_ = 'media__img media__img--thumb').get('href')
           link = 'https://www.carpages.ca' + landing_page
           name = post.find('h4', class_ = 'hN').text.strip()
           price = post.find('strong', class_ = 'delta').text.strip()
           color = post.find_all('div', class_ = 'grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
           desc = post.find('h5', class_ = 'hN').text
                
           df = df.append({'Link':link, 'Name':name, 'Price':price, 'Color':color, 'Description':desc}, ignore_index=True)
    except:
        pass
           
    next_page = soup.find('a', class_ = 'nextprev').get('href')
   
    # Updating the front page to scrape the next page
    page = requests.get(next_page)
    soup = BeautifulSoup(page.text, 'lxml')
    counter += 1

# Saving the data to a csv     
df.to_csv('C:/Users/Max/Desktop/web scraping course/carpages_data.csv')    
    
