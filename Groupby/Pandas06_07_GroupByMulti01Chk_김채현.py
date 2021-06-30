
# coding: utf-8

# In[1]:


#6. lifeExp, gdpPercap 열의 평균값을 연도, 지역별로 그룹화하여
#한 번에 계산하기


# In[14]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv', sep='\t')

multi_group_var=df.groupby(['year','continent'])['lifeExp']
print(multi_group_var)
print(multi_group_var.mean())
print('<'*50)
print(multi_group_var.mean().count())


# In[13]:


#2중 for문 이용해서 위와 같은 결과 가져오기
#lifeExp, gdpPercap 열의 평균값을 연도, 지역별로 그룹화하여 한 번에 계산하기


# In[16]:


uniList1=df['year'].unique()
uniList2=df['continent'].unique()

print(uniList1,'\n=======>')

for idx in uniList:
    print(idx, "=====> ① :")
    conList=df[df['continent']==idx]
    print(len(conList), '\n======> ② \n:', conList.head(3), '\n======> ③:', conList.shape)
    print(conList['pop'].mean())
   

year  continent
1952  Africa       39.135500
      Americas     53.279840
      Asia         46.314394
      Europe       64.408500
      Oceania      69.255000


# In[61]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv', sep='\t')

uniList1=df['year'].unique()
uniList2=df['continent'].unique()
uniList2.sort()

print(uniList1,'\n=======>')
print(uniList2,'\n=======>')

for i in uniList1:
    yearList=df[df['year']==i]
    for j in uniList2:
        conList=yearList[df['continent']==j]#이 줄 틀렸음
        print(f"{i}년 {j:^10}지역 기대수명 평균 : {conList['lifeExp'].mean():.2f}")#민교님

