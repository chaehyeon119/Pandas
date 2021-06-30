
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


# In[17]:


print(subset.tail())#country, continent, year 밑에서 5개 출력


# In[18]:


#dataframe을 하나 형성함 


# In[19]:


import pandas as pd


# In[20]:


df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
df


# In[21]:


df.loc['viper'] #df.iloc[0]
#라벨명으로 가져올 때는 loc, 
#몇 번째 행을 'ex. [0]' 가지고 오고 싶으면
#iloc써야함


# In[22]:


df.loc[0] #loc를 숫자로 가져오면 에러남


# In[23]:


df.loc[['viper', 'sidewinder']]


# In[24]:


df.loc['cobra', 'shield']#cobra의 shield값을 가져와라


# In[25]:


df.loc['cobra':'viper', 'max_speed']
# 라벨로 인덱싱하면  [a :b] b포함으로 옴
#숫자로[1:3]이면 1~2만 포함
#코브라부터 바이퍼까지


# In[26]:


df.loc[[False, False, True]] #3번째 값 가져옴


# In[28]:


df.loc[df['shield']>6]#6이상의 shield 값을 가진 것을 가져옴


# In[30]:


df.loc[df['shield']>6,['max_speed']]
#shield에서 6 이상인 값 중에 max_speed 출력

