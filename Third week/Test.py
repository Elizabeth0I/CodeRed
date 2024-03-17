#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[1]:


import streamlit as st 
from streamlit_jupyter import StreamlitPatcher, tqdm
StreamlitPatcher().jupyter() 


# In[2]:


import os


# In[10]:


#/Users/elizabeth/Downloads

Test1 = pd.read_csv('/Users/elizabeth/Downloads/mieszkania_mac_linux.csv')
Test1.head()


# In[12]:


Test=Test1.groupby(Test1['Rok'])['Wartosc'].mean()
print(Test.to_markdown())


# In[ ]:


st.bar_chart(Test)

