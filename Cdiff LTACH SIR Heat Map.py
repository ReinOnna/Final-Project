#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


matplotlib.use('nbagg')
print(matplotlib.get_backend())


# In[16]:


import matplotlib.pyplot as plt


# In[17]:


df = pd.read_csv('C:/Users/surfe/Desktop/Cdiff SIR LTACH.csv')
print(df.head(5))


# In[18]:


state = ((np.asarray(df['State'])).reshape(5,10))
LTACH = ((np.asarray(df['LTACH'])).reshape(5,10))


# In[19]:


print(state)
print(LTACH)


# In[20]:


piv = df.pivot(index='Xcols', columns='Yrows', values='LTACH')
print(piv)


# In[21]:


labels = (np.asarray(["{0} \n {1:2g}".format(st, value) 
                     for st, value in zip(state.flatten(), 
                                         LTACH.flatten())])).reshape(10,5)


# In[22]:


labels.shape


# In[10]:


piv.shape


# In[25]:


fig, ax = plt.subplots(figsize=(12,8))
ax.set_title('C.diff Long Term Acute Care Hospitals Standardized Infection Ratio for 2015', fontdict = {'fontsize' : '18', 'fontweight' : '4'})

ttl = ax.title
ttl.set_position([0.5,1.05])

ax.set_xticks([])
ax.set_yticks([])

ax.axis('off')

sns.heatmap(piv, annot=labels, fmt="", cmap='coolwarm', linewidths=0.30, ax=ax) 
plt.show()

fig.savefig("Cdiff LTACH HM.png")


# In[ ]:





# In[ ]:




