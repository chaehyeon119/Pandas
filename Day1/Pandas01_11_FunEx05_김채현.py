
# coding: utf-8

# 함수의 결괏값은 언제나 하나이다.
# 튜플값 하나인(a+b, a*b)로 돌려준다.

# In[7]:


def add_and_mul(a,b):
    return a+b,a*b

result=add_and_mul(3,4)
print(result)

