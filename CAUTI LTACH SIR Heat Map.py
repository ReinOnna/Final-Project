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


df = pd.read_csv('C:/Users/surfe/Desktop/Cauti SIR LTACH.csv')
print(df.head(5))


# In[5]:


state = ((np.asarray(df['State'])).reshape(5,10))
LTACH = ((np.asarray(df['LTACH'])).reshape(5,10))


# In[6]:


print(state)
print(LTACH)


# In[7]:


piv = df.pivot(index='Xcols', columns='Yrows', values='LTACH')
print(piv)


# In[8]:


labels = (np.asarray(["{0} \n {1:2g}".format(st, value) 
                     for st, value in zip(state.flatten(), 
                                         LTACH.flatten())])).reshape(10,5)


# In[9]:


labels.shape


# In[10]:


piv.shape


# In[13]:


fig, ax = plt.subplots(figsize=(12,8))
ax.set_title('CAUTI Long Term Acute Care Hospitals Standardized Infection Ratio for 2015', fontdict = {'fontsize' : '18', 'fontweight' : '4'})

ttl = ax.title
ttl.set_position([0.5,1.05])

ax.set_xticks([])
ax.set_yticks([])

ax.axis('off')

sns.heatmap(piv, annot=labels, fmt="", cmap='coolwarm', linewidths=0.30, ax=ax) 
plt.show()

fig.savefig("CAUTI LTACH HM.png")


# In[ ]:





# In[ ]:




