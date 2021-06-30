
# coding: utf-8

# In[29]:


import pandas
deptDB=pandas.read_csv('C:/WSHongIk2021/data/sawonDB/deptDB.csv',names=['deptno','dname','loc'],header=None)
gogekDB=pandas.read_csv('./data/sawonDB/gogekDB.csv',names=['sabun','saname','deptno','sajob','sahire','sapay','sasex','samgr'],header=None)
sawonDB=pandas.read_csv('./data/sawonDB/sawonDB.csv',names=['gobun','goname','gotel','gojumin','godam'],header=None)

print(deptDB)
print(gogekDB)
print(gogekDB)
# deptDB.columns=['deptno','dname','loc']#4x3
# gogekDB.columns=['sabun','saname','deptno','sajob','sahire','sapay','sasex','samgr']
# sawonDB.columns=['gobun','goname','gotel','gojumin','godam']


# In[46]:


# print(deptDB)
# print(gogekDB)
# print(gogekDB)
# print(deptDB.replace("'",' '))
gogekDB = gogekDB.replace('\'','',regex=True)
print(gogekDB)


# In[47]:


sawonDB=sawonDB.replace('\'','',regex=True)
print(sawonDB)


# In[49]:


gogekDB=gogekDB.replace('\'','',regex=True)
print(gogekDB)


# In[50]:



#문제1] SawonDB 데이터에서 입사년도가 88년도인 사원 출력.
#문제2] SawonDB 데이터에서 4월에 입사한 사원을 출력
#문제3] SawonDB 데이터에서 사원번호가 짝수인 사람만 출력
#문제4]SawonDB 데이터에서 직위별 급여 평균 출력
#문제5]SawonDB 데이터에서 직위별, 성별 평균 출력

