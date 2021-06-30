
# coding: utf-8

# In[1]:


#Pandas06_03_GroupByChk01_김채현


# In[18]:


df=pandas.read_csv('./data/gapminder.tsv', sep='\t')


# In[19]:


df


# In[17]:


type(df)
#데이터프레임 형식


# In[4]:


type(df['pop'])#하나만 가져오니까 시리즈형식으로 뜸


# In[10]:


grouped_year_df=df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df['pop'])


# In[11]:


grouped_year_df['pop'].mean()

