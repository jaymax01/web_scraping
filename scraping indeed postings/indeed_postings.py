# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:48:58 2021

@author: Max
"""
# Importing libraries for parsing HTML and entering search terms into fields
import re
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Loading the web driver and connecting to indeed.com
driver = webdriver.Chrome("C:/Users/Max/Downloads/chromedriver.exe")
driver.get('https://WWW.indeed.com/')
driver.find_element_by_xpath('//*[@id="ssrRoot"]/div[3]/div[16]/span/a').click()

# Typing search results into the search fields
job_title = 'Data analyst'
where = ''
title = driver.find_element_by_xpath('//*[@id="text-input-what"]')
title.send_keys(job_title)
title.send_keys(Keys.ENTER)

loc = driver.find_element_by_xpath('//*[@id="where"]')
loc.send_keys(where)
loc.send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="fj"]').click()

# Defining a dataframe to collect all the postings
df = pd.DataFrame({'Link':[''], 'title':[''], 'company':[''], 'salary':[''], 'date':[''], 'location':['']})


# scrolling through each page and collecting the job postings per page
while True:
    
        soup = BeautifulSoup(driver.page_source, 'lxml')
        listings = soup.find('td', {'id':'resultsCol'})
        postings = listings.find_all('div', class_ = 'jobsearch-SerpJobCard unifiedRow row result clickcard')
    
    
        for post in postings:
            try:
                link = post.find('a').get('href')
                full_link = 'https://www.indeed.com'+ link
                title = post.find('a', re.compile('title')).text.strip()
                company = post.find('span', class_ = 'company').text.strip()
                try:
                    salary = post.find('span', class_ = 'salaryText').text.strip()
                except:
                    salary = 'N/A'
                date = post.find('span', class_ = 'date date-a11y').text.strip()
                try:
                    location = post.find('span', class_ = 'location accessible-contrast-color-location').text.strip()
                except:
                    location = 'N/A'
                df = df.append({'Link':full_link, 'title':title, 'company':company, 'salary':salary, 'date':date, 'location':location}, ignore_index=True)
            except:
                pass
        try:
            driver.find_element_by_xpath('//*[@id="resultsCol"]/nav/div/ul/li[6]/a').click()
        except:
            break
        
df.to_csv('C:/Users/Max/Desktop/Web scraping/indeed_job_listings.csv')

    