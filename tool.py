#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[7]:


def get_soup(url):
    try:
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text,'lxml')
            return soup
        else:
            print('網頁取得失敗',resp.status_code )
    except Exception as e:
        print('網址錯誤',e)


# In[ ]:




