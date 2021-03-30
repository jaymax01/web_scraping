# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:26:08 2021

@author: Max
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd 
import time

# Loading the driver and the saerch results
driver = webdriver.Chrome('C:/Users/Max/Downloads/chromedriver.exe')
driver.get('https://www.google.com')

english = driver.find_element_by_xpath('//*[@id="SIvCob"]/a').click()
box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('Union Los Angeles Outerwear Section')
box.send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3').click()
driver.find_element_by_xpath('//*[@id="topNav"]/li[3]/a').click()

# Scrolling through the pages until the end of the page
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if last_height == new_height:
        break
    last_height = new_height

#Imports the HTML of the webpage into python  
soup = BeautifulSoup(driver.page_source, 'lxml')

#grabs the HTML of the products and then each product
section = soup.find('div', {'id':'main', 'role':'main'})
postings = section.find_all('li')

df = pd.DataFrame({'Link':[''], 'Vendor':[''],'Title':[''], 'Price':['']})

#Getting the information from the postings
for post in postings:
    try:
            link = post.find('a').get('href')
            vendor = post.find(class_ = 'cap-vendor').text
            title = post.find(class_ = 'cap-title').text
            price = post.find(class_ = 'cap-price').text
            df = df.append({'Link':link, 'Vendor':vendor,'Title':title, 'Price':price}, ignore_index = True)
    except:
        pass

# fixes the link of the first 4 products on the page    
df['Link'][4:] = 'https://store.unionlosangeles.com'+df['Link'][4:]

# Saving the dataframe to a csv file
df.to_csv("C:/Users/Max/Desktop/web scraping course/javascript_page.csv")