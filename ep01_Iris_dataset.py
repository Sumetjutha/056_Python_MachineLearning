#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets
import pandas as pd


# In[2]:


datasets.load_iris()


# In[3]:


iris_dataset = datasets.load_iris()


# In[4]:


type(iris_dataset)


# In[5]:


print(iris_dataset.keys())


# In[6]:


iris_dataset['target']


# In[7]:


iris_dataset['target_names']


# In[8]:


print(iris_dataset['DESCR'])


# In[9]:


iris_dataset['data']


# In[10]:


iris_dataset['data'].shape


# In[11]:


iris_dataset['data'][0:20]

