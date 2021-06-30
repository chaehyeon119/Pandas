
# coding: utf-8

# In[1]:


#Pandas05_05_DataFilterRows02iloc_김채현


# In[3]:


import pandas as pd
mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
df = pd.DataFrame(mydict)
df


# In[4]:


type(df.iloc[0])#한 줄은 Series로 뜸


# In[5]:


df.iloc[0]


# In[6]:


df.iloc[[0]]
#dataframe형으로 옴 [[]]


# In[7]:


type(df.iloc[[0]])


# In[15]:


df.iloc[[0,2]]#인덱싱 0,2모두 가져옴
#컬렉션 행이라 행으로 옴


# In[9]:


df.iloc[:3]#0부터 2까지


# In[13]:


df.iloc[[True,False, True]]#첫번째, 세번째 값만 가져옴


# In[14]:


df.iloc[0,1]
#df.ioc[0,1]0형 1열의 값


# In[16]:


df.iloc[[0,2],[1,3]]
#0,2번째 행의 1,3열만 가져오기


# In[17]:


df.iloc[1:3, 0:3]
#1~2까지의 행의 0부터 2까지의 열 가져오기


# In[18]:


df.iloc[:,[True, False, True, False]]
#행은 다 가져오고 첫번째 세번째 열만 가져오기

