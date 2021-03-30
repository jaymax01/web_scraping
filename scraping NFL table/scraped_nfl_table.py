# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:07:49 2021

@author: Max
"""
# Importing libraries for requesting and parsing HTML 
import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

# Loading the NFL standings for 2019 season
url = 'https://www.nfl.com/standings/league/2019/reg/'
page = requests.get(url)

# Parsing the data table
soup = BeautifulSoup(page.text, 'lxml')
#print(soup)

# Collecting the data tags for the table
table = soup.find('div', class_ = 'd3-o-table--horizontal-scroll')
#print(table)

# Collecting coloumn data
col_tags = table.find('tr')

# Collecting the headers and creating a blank dictionary for each column
headers = col_tags.find_all('th')

header_list = []
for i in headers:
    temp = i.text
    temp_2 = temp.strip()
    header_list.append(temp_2)

df_dict = {} # needed
for i in header_list:
    df_dict[i] = None
    
print(df_dict)

# Storing the list of teams in the league
teams_list = []

teams = table.find_all('div', 'd3-o-club-fullname')
for i in teams:
    temp = i.text
    print(temp)
    temp_1 = temp.strip()
    temp_2 = temp_1.strip('\n            xz*')
    teams_list.append(temp_2)

teams_list_rev = teams_list[: :-1]  # needed
#print(teams_list_rev)

# Collecting the stats for each team 
stats = table.find_all('tr')
#print(stats)
stats_list = [] # needed 
for j in range(-1, -len(stats), -1):
    temp = stats[j].find_all('td')
    #print(temp[1:])
    temp_2 = [a.text.strip('\n              ') for a in temp[1:]]
    stats_list.append(temp_2)
    
stats_array = np.array(stats_list)
#print(stats_array[:,0])

# Putting all of the information into a dataframe
df_dict['NFL Team'] = teams_list_rev
print(df_dict)

j = 0
for i in header_list[1:]:
    df_dict[i] = stats_array[:,j]
    j = j + 1
        
print(df_dict)
df = pd.DataFrame(df_dict)
print(df)

# Saving the table to a csv file
df.to_csv("C:/Users/Max/Desktop/Web scraping_class/nfl_table.csv")

