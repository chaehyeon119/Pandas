
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


# In[33]:


import pandas as pd

#HTML 파일 경로 or 웹 페이지 주소를 url 변수에 저장
url='./DataSet/Pandas04_08_Test01_김채현.html'

#HTML 웹페이지의 표(table)를 가져와서 데이터프레임으로 변환
tables=pd.read_html(url)

#표(table)의 개수 확인
print(len(tables), '\n==>')

print(tables,'\n==>')

#tables 리스트의 원소를 teration하면서 각각 화면 출력
for i in range(len(tables)):
    print('tables[%s]'%i,'\n')
    print(tables[i],'\n')

#파이썬 패키지 정보가 들어 있는 두 번째 데이터프레임을 선택하여
#df 변수에 저장
df=tables[1]
print(df.columns,'\n')

      

