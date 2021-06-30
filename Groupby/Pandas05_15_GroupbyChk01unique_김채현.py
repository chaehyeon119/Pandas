
# coding: utf-8

# In[ ]:


#Pandas05_14_uniqueChk01_김채현


# In[8]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv', sep='\t')

s=pd.Series([1,3,5,7,7])
s.unique()
print(s.unique())
print(s.nunique())


# In[9]:


print(df.head(n=10))


# In[10]:


print(df.groupby('year')['lifeExp'].mean())
#중복되는 year을 묶고 lifeExp값을 평균냄


# In[11]:


df['year'].unique()


# In[12]:


uniList=df['year'].unique()
print(type(uniList))
print(uniList,'\n=======>')

