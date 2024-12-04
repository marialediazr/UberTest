#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import chardet


# In[2]:


st.title("Dashboard")


# In[3]:


DATE_COLUMN="date/time"


# In[4]:


with open('movies.csv', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    print(result) 


# In[5]:


movies = pd.read_csv('movies.csv', encoding='ISO-8859-1')

movies.to_csv('movies_utf8.csv', index=False, encoding='utf-8')


# In[6]:


movies.head(15)


# In[7]:


movies['year'] = movies['title'].str.extract(r'\((\d{4})\)')
movies.head()


# In[8]:


ratings = pd.read_csv("ratings.csv")


# In[9]:


with open('tags.csv', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    print(result) 


# In[10]:


tags = pd.read_csv('tags.csv', encoding='Windows-1252')

tags.to_csv('tags_utf8.csv', index=False, encoding='utf-8')


# In[11]:


average_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()
average_ratings.columns = ['movieId', 'average_rating']
average_ratings['average_rating'] = average_ratings['average_rating'].round(1)
print(average_ratings)


# In[12]:


movies2 = movies.copy()


# In[13]:


movies2.drop('title', axis=1, inplace=True)


# In[14]:


movies2.head()


# In[15]:


movies2['year'] = movies2['year'].astype(int)


# In[16]:


movies_per_year = movies2.groupby('year').size()

plt.figure(figsize=(10, 6))
plt.plot(movies_per_year.index, movies_per_year.values, marker='o')
plt.title('Number of Movies Released Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')

custom_ticks = list(range(movies_per_year.index.min(), movies_per_year.index.max() + 1, 5))
plt.xticks(custom_ticks)
plt.xticks(rotation=90, fontsize=8)

plt.grid(True)
plt.show()

