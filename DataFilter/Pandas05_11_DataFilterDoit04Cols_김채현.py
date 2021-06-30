
# coding: utf-8

# In[1]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv', sep='\t')


# In[2]:


print(df.head(3))


# In[3]:


print(df.iloc[1])


# In[4]:


print(df.iloc[99])


# In[5]:


print(df.iloc[-1])
#맨 뒤에서 첫번째


# In[6]:


print(df.tail(1))
print(df.shape)
print(df.iloc[1703])


# In[9]:


print(df.iloc[[0,99,999]])


# In[10]:


df.head(3)


# In[12]:


subset=df.loc[:,['year', 'pop']]
print(subset.head())


# In[13]:


subset=df.iloc[:,[2,4,-1]]#2:year,4:pop,-1:gdp
print(subset.head())

