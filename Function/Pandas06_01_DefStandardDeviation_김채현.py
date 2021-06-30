
# coding: utf-8

# In[52]:


#Pandas06_01_DefStandardDeviation_김채현
#중앙값 구하기
a=[28,31,24,25,30,32,20,30,31,26,31]
total=0

#정렬하고 가운데의 값을 가져와야함
def mMedian():
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                temp=0
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                
    if len(a)%2==0:
        return (a[int(len(a)/2)]+a[int(len(a)/2)+1])/2
    #나누기 연산을 하면 늘 소수점이 붙음 정수로 표현하려고 int사용
               
    return a[int(len(a)/2)]#0부터 세는거니까
print(mMedian())#함수 호출할 때 괄호 꼭


# In[33]:


#평균
a=[28,31,24,25,30,32,20,30,31,26,31]


def mMean():
    total=0
    for i in a:
        total=total+i
        mMean=total/len(a)
    return mMean
print(mMean())


# In[53]:


#편차(관측값-관측값의 평균) mDeviation
def mDeviation(a,mMean):
    
    
#분산(variance)
def mVariance(listValue, avg):
##분산은 편차(관측값-관측값의 평균)의 제곱에(관측수-1)




    
#표준편차(#표준편차: 분산의 제곱근)
def mStandardDeviation():
    pa
#범위(Range): 최대값과 최소값의 차이


# In[ ]:


import pandas as pd

lst=[28,31,24,25,30,32,20,30,31,26,31]
da=pd.Series(lst)
print('Built-in')

