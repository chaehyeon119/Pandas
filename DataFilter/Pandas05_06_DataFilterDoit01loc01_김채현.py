
# coding: utf-8

# In[1]:


#Pandas05_06_DataFilterDoit01loc01_김채현


# In[2]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv', sep='\t')


# In[3]:


df.head(3)


# In[4]:


df.shape#행렬확인


# In[5]:


loc00=df.loc[0]


# In[8]:


print(loc00);type(loc00)#loc는 행추출


# In[10]:


df.loc[90:100]#loc는[a:b] a부터 b까지 모두 출력


# In[11]:


print(df.loc[99])#99번째 행 출력


# In[12]:


df.tail(3)


# In[13]:


#loc는 라벨이라 -개념이 없음
print(df.loc[-1])


# In[14]:


len(df)#행의 개수

