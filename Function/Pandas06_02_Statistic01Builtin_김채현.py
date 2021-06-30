
# coding: utf-8

# In[ ]:


#Pandas06_02_Statistic01Builtin_김채현


# In[1]:


import pandas as pd

lst=[28,31,24,25,30,32,20,30,31,26,31]
da=pd.Series(lst)
print('Built-in 정렬 sort_value() : \n', da.sort_values(ascending=True))
print('Built-in 평균 mean() : %d' %da.mean())
print('Built-in 중위수 median() : %d'%da.median())
print('Built-in 분산 var() : %d'%da.var())
print('Built-in 표준편차 std() : %d' %da.std())
print('Built-in 제1사분위수 quantile() : %d' %da.quantile(q=0.25))
print('Built-in 제2사분위수 quantile() : %d' %da.quantile(q=0.5))
print('Built-in 제3사분위수 quantile() : %d' %da.quantile(q=0.75))
print('=*50')
da.describe()

