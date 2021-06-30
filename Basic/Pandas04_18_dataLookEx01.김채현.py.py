
# coding: utf-8

# In[21]:



#import pandas as pd
#file_pathExcel='./DataSet/datalabPractice01.xlsx'
#dfExcel=pd.read_excel(file_pathExcel)
#print(dfExcel)  #\ 너무 길어서 쓰는거
df2=pd.read_excel('./DataSet/datalabPractice01.xlsx',                    sheet_name='Sheet1', usecols=[0,1,2], skiprows=[0],                    skipfooter=2, header=None)
print(df2)
df3=pd.read_excel('./DataSet/datalabPractice01.xlsx',                    sheet_name='Sheet1', usecols=[0,1,2], skiprows=[1],                    skipfooter=2, header=None)
print(df3)
#usecols=열을 의미 ex. [0,1]이면 왼쪽 두 세로줄만 나옴
#skipfooter은 맨 뒤 행을 지움 ex. skipfooter=1은 맨 뒤 가로줄 한 줄 빠짐
#skiprows=[n] 0~ n번째 열 사라짐/가로줄 사라짐


# In[29]:


df=pd.read_json('./DataSet/read_json_sample.json')
print(df,'\n')

print(df.index) #행 출력
print(df.columns) #열 출력


# In[34]:


import pandas as pd

#HTML 파일 경로 or 웹 페이지 주소를 url 변수에 저장
url='./DataSet/Pandas04_08_Test01_김채현.html'

#HTML 웹페이지의 표(table)를 가져와서 데이터프레임으로 변환
tables=pd.read_html(url)

#표(table)의 개수 확인
print(len(tables), '\n==>')

print(tables,'\n==>')

#tables 리스트의 원소를 iteration(상호작용)하면서 각각 화면 출력
for i in range(len(tables)):
    print('tables[%s]'%i,'\n')
    print(tables[i],'\n')

#파이썬 패키지 정보가 들어 있는 두 번째 데이터프레임을 선택하여
#df 변수에 저장
df=tables[1]
print(df.columns,'\n')

      


# In[40]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv', sep='\t')
#sep='\t'는 탭으로 구별한다는 뜻 tsv는 탭으로 구별해야함
print(df)


# In[41]:


'''
데이터 불러오기

df라는 변수에 저장
데이터추출/불러온 데이터 확인하기/
head:데이터 프레임에서 가장 앞에 있는 5개의 행을 출력한다.
head, tail, info, type, dtypes, shape, index, columns
앞     뒤
'''


# In[44]:


import pandas as pd
df=pd.DataFrame({'animal':['alligator', 'bee', 'falcon','lion','monkey'
                          , 'parrot','shark','whale','zebra']})
print(df)
print(df.head())#5개만 출력
print()
print(df.head(3))#앞에서 3개만 출력
print()
print(df.head(-3))#뒤에서 3개 뺀 값 출력


# In[62]:


import pandas as pd
df=pd.DataFrame({'col1':[1,2],'col2':[3,4]})
print(df)

df.shape #몇 행 몇 열인지
print()
df1=pd.DataFrame({'col1':[1,2],'col2':[3,4],'col3':[5,6]})
df1.shape
print(df1)


# In[51]:


import pandas as pd


# In[61]:


df=pd.DataFrame({'col1':[1,2],'col2':[3,4],'col3':[5,6]})


# In[53]:


print(df)


# In[60]:


df.shape


# In[56]:


df1=pd.DataFrame({'col1':[1,2],'col2':[3,4],'col3':[5,6]})


# In[63]:


print(df1)


# In[65]:


df1=pd.DataFrame({'col1':[1,2],'col2':[3,4],'col3':[5,6]})
df1.shape


# In[68]:


import pandas as pd
df=pd.read_csv('./data/gapminder.tsv', sep='\t')
#sep='\t'는 탭으로 구별한다는 뜻 tsv는 탭으로 구별해야함
df.shape


# In[70]:


df=pd.DataFrame({'float':[1.0],
                'int':[1],
                'datetime':[pd.Timestamp('20180310')],
                 'string':['foo']})
print(df)
df.dtypes


# In[71]:


int_values=[1,2,3,4,5]
text_values=['alpha','beta','gamma','delta','epsilon']
float_values=[0.0,0.25,0.5,0.75,1.0]
df=pd.DataFrame({'int_col':int_values,'text_col':text_values,
                'float_col':float_values})
df


# In[72]:


df.info(verbose=False)


# In[73]:


df.dtypes


# In[74]:


df.info()


# In[75]:


df.info(verbose=True)


# In[77]:


#groupby 겹치는 종류가 많을 때 사용함 ex) 남자별 평균, 여자별 평균
#판다스에서 mean은 평균이라는 뜻


# In[78]:


import pandas as pd


# In[80]:


df=pd.DataFrame({'Animal':['Falcon','Falcon',
                         'Parrot','Parrot'],
                'Max Speed':[380.,370.,24.,26.]})
df


# In[81]:


df.groupby(['Animal']).mean()#판다스에서 mean은 평균이라는 뜻


# In[82]:


#len(df)와 df[0:5]랑 같음
#df[len(df)-5:len(df)+1] 1704-5(1699):1704+1
#=df.tail()과 같은 결과


# In[83]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv', sep='\t')
#sep='\t'는 탭으로 구별한다는 뜻 tsv는 탭으로 구별해야함
print(df.shape)#(1704,6)
print(df.shape[0])#1704
print(df.shape[1])#6


# In[84]:


len(df)


# In[85]:


df.head() #앞에서부터 5개 가져옴


# In[86]:


df[0:5]#0~4


# In[87]:


df.head(n=7)#0~7


# In[88]:


df.tail()


# In[92]:


df[len(df)-5:len(df)+1]#1704-5(1699):1704+1(1705)


# In[90]:


df.tail(n=7)


# In[93]:


#데이터 자료형을 확인
type(df)


# In[94]:


#데이터프레임의 열 확인
print(df.columns)


# In[98]:


#데이터프레임의 행 확인
df.index


# In[99]:


#데이터프레임을 구성하는 값의 자료형을 확인
print(df.dtypes)


# In[100]:


#데이터 집합과 각 열들의 자료형을 자세히 확인
print(df.info())


# In[101]:


#(행, 열) 크기를 알 수 있습니다.
df.shape

