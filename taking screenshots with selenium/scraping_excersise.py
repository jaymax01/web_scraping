# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:58:56 2021

@author: Max
"""
import re
from bs4 import BeautifulSoup
import requests

url = 'https://www.marketwatch.com/investing/stock/amzn?mod=over_search'

page = requests.get(url)
#print(page.text)

soup = BeautifulSoup(page.text, 'lxml')
#print(soup)

# Price of the stock
price = soup.find_all('div', class_ ='intraday__data')[0]
print('The stock price is : {}'.format(price.find('h3').text) )
print()


# Closing price of the stock
closing_price = soup.find('td', class_ = re.compile('u-semi'))
print('The closing price is :', closing_price.text)
print()


# 52 week range (lower, upper)
week_range = soup.find_all('div', class_ = 'range__header')[2]
week_range_2 = week_range.find_all('span', class_= 'primary')
print('The 52 week range for the stock')
for i in week_range_2:
    print(i.text)
print()   
  

# Analyst rating
rating = soup.find_all('div', class_ = 'analyst__chart')[0]
rating_2 = rating.find_all('li', class_ = 'analyst__option active')[0]
print('The analyst rating for the stock is :', rating_2.string)

