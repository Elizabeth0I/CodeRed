#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd


# In[7]:


import streamlit as st 
from streamlit_jupyter import StreamlitPatcher, tqdm
StreamlitPatcher().jupyter() 


# In[2]:


import os


# In[12]:


#/Users/elizabeth/Downloads

df = pd.read_csv('/Users/elizabeth/Downloads/mieszkania_mac_linux.csv')
df.head()


# In[16]:


dfy = df.groupby(df['Rok'])['Wartosc'].mean()
print(dfy.to_markdown())


# In[21]:


st.dataframe(dfy.to_frame())

