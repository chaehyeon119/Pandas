
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


# In[15]:


len(df)#행의 개수


# In[ ]:


#Pandas05_07_DataFilterDoit02Tail_김채현


# In[16]:


number_of_rows=df.shape[0]#(1704,6)의 0번째 값
print(number_of_rows,'\n\n')

last_row_index=number_of_rows-1#1704-1
print(df.loc[last_row_index])


# In[21]:


print(df.loc[len(df)-1])#1703번째의 값


# In[18]:


print(df.tail(n=1))


# In[19]:


print(df.tail(n=2))#뒤에서 2개


# In[22]:


print(df.loc[[0,99,999]])#0,99,999번째 행 가져오기

