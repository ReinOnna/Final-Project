#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


matplotlib.use('nbagg')
print(matplotlib.get_backend())


# In[15]:


import matplotlib.pyplot as plt


# In[16]:


df = pd.read_csv('C:/Users/surfe/Desktop/Cauti SIR ACH.csv')
print(df.head(5))


# In[17]:


state = ((np.asarray(df['State'])).reshape(5,10))
ACH = ((np.asarray(df['ACH'])).reshape(5,10))


# In[18]:


print(state)
print(ACH)


# In[19]:


piv = df.pivot(index='Xcols', columns='Yrows', values='ACH')
print(piv)


# In[20]:


labels = (np.asarray(["{0} \n {1:2g}".format(st, value) 
                     for st, value in zip(state.flatten(), 
                                         ACH.flatten())])).reshape(10,5)


# In[21]:


labels.shape


# In[22]:


piv.shape


# In[24]:


fig, ax = plt.subplots(figsize=(12,8))
ax.set_title('CAUTI Acute Care Hospitals Standardized Infection Ratio for 2015', fontdict = {'fontsize' : '18', 'fontweight' : '4'})

ttl = ax.title
ttl.set_position([0.5,1.05])

ax.set_xticks([])
ax.set_yticks([])

ax.axis('off')

sns.heatmap(piv, annot=labels, fmt="", cmap='coolwarm', linewidths=0.30, ax=ax) 
plt.show()

fig.savefig("CAUTI ACH HM.png")


# In[ ]:





# In[ ]:




