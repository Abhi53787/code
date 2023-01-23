#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


dt = pd.read_csv('pokemon_data.csv')


# In[5]:


print(dt)


# In[7]:


print(dt.head(10))


# In[11]:


dt.columns


# In[20]:


oo=(dt[['Name','Speed']])


# In[21]:


print(oo)


# In[22]:


print(oo[:5])


# In[27]:


print(oo[1:100])


# In[35]:


dt.loc[dt['Name']=="Muk"]


# In[36]:


dt.loc[dt['Name']=='Muk']


# In[37]:


dt.describe()


# In[40]:


dt.sort_values("Name", ascending=True)


# In[41]:


#making changes
dt.head(5)


# In[49]:


dt['Total']=dt['HP']+dt['Attack']+dt['Defense']+dt['Speed']


# In[51]:


print(dt['Total'])


# In[ ]:




