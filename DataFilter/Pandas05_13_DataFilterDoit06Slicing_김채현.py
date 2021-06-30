
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


# In[15]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv', sep='\t')
small_range=list(range(5))
print(small_range)


# In[16]:


print(type(small_range))


# In[17]:


df.head(3)


# In[18]:


subset=df.iloc[:, small_range]
print(subset.head())


# In[19]:


small_range=list(range(3,6))#3,4,5
print(small_range)


# In[25]:


subset=df.iloc[:,small_range]
print(subset.head())


# In[24]:


small_rage=list(range(0,6,2))#0,2,4
subset=df.iloc[:,small_range]
print(subset.head())


# In[ ]:


#Pandas05_13_DataFilterDoit06Slicing_김채현


# In[26]:


subset=df.iloc[:,:3]#0,1,2
print(subset.head())


# In[27]:


subset=df.iloc[:,0:6:2]#0,2,4
print(subset.head())


# In[28]:


df.head(3)


# In[29]:


print(df.iloc[[0,99,999],[0,3,5]])


# In[30]:


print(df.loc[[0,99,999], ['country', 'lifeExp','gdpPercap']])


# In[31]:


print(df.loc[10:13, ['country','lifeExp','gdpPercap']])


# In[32]:


print(df.iloc[10:13,[0,3,-1]])

