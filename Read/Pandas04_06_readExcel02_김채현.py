
# coding: utf-8

# In[20]:



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

