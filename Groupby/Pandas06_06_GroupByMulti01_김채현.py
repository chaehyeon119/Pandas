
# coding: utf-8

# In[1]:


#6. lifeExp, gdpPercap 열의 평균값을 연도, 지역별로 그룹화하여
#한 번에 계산하기


# In[6]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv', sep='\t')
df


# In[9]:


multi_group_var=df.groupby(['year','continent'])['lifeExp']
print(multi_group_var)
print(multi_group_var.mean())
print('<'*50)
print(multi_group_var.mean().count())

