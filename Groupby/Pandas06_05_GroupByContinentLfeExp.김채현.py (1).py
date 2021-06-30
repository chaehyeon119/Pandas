
# coding: utf-8

# In[ ]:


#연도로 그룹하고 인구수의 평균을 확인(unique 방법과, built-in 방법 2가지로 구현)


# In[2]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv', sep='\t')
df


# In[17]:


uniList=df['continent'].unique()

print(type(uniList))
print(uniList,'\n=======>')

for idx in uniList:
    print(idx, "=====> ① :")
    conList=df[df['continent']==idx]
    print(len(conList), '\n======> ② \n:', conList.head(3), '\n======> ③:', conList.shape)
    print(conList['pop'].mean())


# In[20]:


import pandas as pd
da=pd.Series(conList['lifeExp'])
print('Built-in 평균 mean() : %d' %da.mean())

