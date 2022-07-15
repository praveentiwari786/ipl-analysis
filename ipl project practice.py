#!/usr/bin/env python
# coding: utf-8

# # project:Finding insights and analysing Ipl data set

# In[1]:


#IMPORTING ALL LIBRARIES
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


#LOADING THE IPL DATASET
IPL=pd.read_csv("IPL data.csv")
IPL
#finding null values
IPL.isnull().sum()
#TOTAL ROWS and COLUMNS
IPL.shape
#looking top five records
IPL.head()


# ## Preprocessing the IPL dataset

# In[3]:


#Checking the frequency of most player_of_match
IPL["player_of_match"].value_counts()
#Top 10 most player_of_match
IPL["player_of_match"].value_counts()[0:10]
#getting the names of top 10 player_of_match
list(IPL["player_of_match"].value_counts()[0:10].keys())


# In[4]:


#checking the BARPLOT of top 10 player_of_match with respect to names and their winning counts:
plt.figure(figsize=(12,8))
plt.bar(list(IPL["player_of_match"].value_counts()[0:10].keys()),list(IPL["player_of_match"].value_counts()[0:10]),color="Red")
plt.show()        


# In[5]:


#Frequency of result
IPL["result"].value_counts()


# In[6]:


#Finding out the total toss win by each time
IPL["toss_winner"].value_counts()


# In[7]:


#Extracting the record of teams won after batting first
Batting_first=IPL[IPL["win_by_runs"]!=0]
Batting_first[0:10]


# In[8]:


#making HISTOGRAM for teams batting first and won with respect to margin of runs
plt.figure(figsize=(8,8))
plt.hist(Batting_first["win_by_runs"])
plt.title("Distribution of runs")
plt.xlabel("Runs")
plt.show


# In[9]:


#Teams batting first and won total number of matches and making BAR chart
Batting_first["winner"].value_counts()
plt.figure(figsize=(25,15))
plt.bar(list(Batting_first["winner"].value_counts().keys()),list(Batting_first["winner"].value_counts()),color="green")
plt.show


# In[10]:


#Extracting the records when team WON after doing second batting
Batting_second=IPL[IPL["win_by_wickets"]!=0]
Batting_second


# In[11]:


#Creating Bar chart for team won while doing second batting with their team names and winning times
plt.figure(figsize=(20,7))
plt.bar(list(Batting_second["winner"].value_counts().keys()),list(Batting_second["winner"].value_counts()),color="yellow")
plt.show()
        


# In[12]:


#team won after winning toss#importing NUMPY
import numpy as np
toss_and_match_winner=np.sum(IPL["toss_winner"]==IPL["winner"])
toss_and_match_winner
total_matches=np.sum(IPL["id"])
total_matches
#showing with piechart team won percentage of "winning toss with match" out of total matches
plt.figure(figsize=(7,7))
plt.pie((toss_and_match_winner,total_matches),autopct='%1.1f%%')
plt.show()


# In[13]:


#match played in each season
IPL["season"].value_counts()


# In[14]:


#matches played in each city
IPL["city"].value_counts()


# In[23]:


#creating pie chart with respect to winning by doing second batting and doing first batting
plt.figure(figsize=(7,7))
plt.pie((np.sum(IPL["win_by_runs"]),np.sum(IPL["win_by_wickets"])),autopct='%1.1f%%')
plt.show()


# In[ ]:




