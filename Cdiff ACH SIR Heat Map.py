#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


matplotlib.use('nbagg')
print(matplotlib.get_backend())


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv('C:/Users/surfe/Desktop/Cdiff SIR ACH.csv')
print(df.head(5))


# In[7]:


state = ((np.asarray(df['State'])).reshape(5,10))
ACH = ((np.asarray(df['ACH'])).reshape(5,10))


# In[8]:


print(state)
print(ACH)


# In[10]:


piv = df.pivot(index='Xcols', columns='Yrows', values='ACH')
print(piv)


# In[11]:


labels = (np.asarray(["{0} \n {1:2g}".format(st, value) 
                     for st, value in zip(state.flatten(), 
                                         ACH.flatten())])).reshape(10,5)


# In[12]:


labels.shape


# In[13]:


piv.shape


# In[14]:


fig, ax = plt.subplots(figsize=(12,8))
ax.set_title('C.diff Acute Care Hospitals Standardized Infection Ratio for 2015', fontdict = {'fontsize' : '18', 'fontweight' : '4'})

ttl = ax.title
ttl.set_position([0.5,1.05])

ax.set_xticks([])
ax.set_yticks([])

ax.axis('off')

sns.heatmap(piv, annot=labels, fmt="", cmap='coolwarm', linewidths=0.30, ax=ax) 
plt.show()

fig.savefig("Cdiff ACH HM.png")


# In[ ]:





# In[ ]:




