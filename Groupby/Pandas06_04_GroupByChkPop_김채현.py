
# coding: utf-8

# In[ ]:


#기대수명 -> pop으로 변경하기


# In[2]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv', sep='\t')
df


# In[9]:


print(df.groupby('year')['pop'].mean())


# In[10]:


df['year'].unique()
uniList=df['year'].unique()

print(type(uniList))
print(uniList,'\n=======>')


for idx in uniList:
    print(idx, "=====> ① :")
    yearList=df[df['year']==idx]
    print(len(yearList), '\n======> ② \n:', yearList.head(3), '\n======> ③:', yearList.shape)
    print(yearList['pop'].mean())

