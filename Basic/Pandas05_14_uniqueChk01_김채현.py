
# coding: utf-8

# In[ ]:


#Pandas05_14_uniqueChk01_김채현


# In[7]:


import pandas as pd
s=pd.Series([1,3,5,7,7])
s.unique()
print(s.unique())
print(s.nunique())

