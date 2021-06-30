
# coding: utf-8

# In[ ]:


#Pandas05_02_DataFilterCols01_김채현


# In[16]:


import pandas


# In[4]:


df=pandas.read_csv('./data/gapminder.tsv', sep='\t')


# In[5]:


country_df=df['country']
print(type(country_df))#하나니까 시리즈로 출력


# In[6]:


print(country_df.head())#country 위에서 5개 출력


# In[8]:


print(country_df.tail())#country 뒤에서 5개 출력


# In[10]:


subset=df[['country','continent','year']]
print(type(subset))#여러 개니까 DataFrame으로 출력


# In[12]:


print(subset.head())#country, continent, year 위에서 5개 출력


# In[ ]:


print(subset.tail())#country, continent, year 밑에서 5개 출력

