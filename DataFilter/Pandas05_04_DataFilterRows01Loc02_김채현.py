
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


#Pandas05_03 DataFilterRows01Loc01_김채현


# In[19]:


import pandas as pd


# In[20]:


df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
df
#dataframe을 하나 형성함 


# In[21]:


df.loc['viper'] #df.iloc[0]
#라벨명으로 가져올 때는 loc, 
#몇 번째 행을 'ex. [0]' 가지고 오고 싶으면
#iloc써야함


# In[31]:


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


# In[32]:


df.loc[df['shield']>6,['max_speed']]
#shield에서 6 이상인 값 중에 max_speed 출력


# In[33]:


df.loc[['viper','sidewinder'],['shield']]=50
df
#viper, sidewinder의 shield 값을 50으로 변경


# In[35]:


df.loc['cobra']=10
df
#cobra의 값을 10으로 바꾼다


# In[36]:


df.loc[:,'max_speed']=30
df
#모든 값의 max speed를 30으로 변경함


# In[38]:


df.loc[df['shield']>35]=0
df
#shield의 값이 35인 것들의 shield값을 0으로 만듦


# In[43]:


df=pd.DataFrame([[1,2],[4,5],[7,8]],
index=[7,8,9], columns=['max_speed', 'shield'])
df


# In[44]:


df.loc[7:9]
#숫자를 가져오는게 아닌 라벨 7,8,9를 가져오는거라
#9도 포함됨

