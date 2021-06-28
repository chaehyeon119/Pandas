
# coding: utf-8

# In[4]:


def add_mul(choice, *args):
    if choice=='add':
        result=0
        for i in args:
            result=result+i
    elif choice=='mul':
        result=1
        for i in args:
            result=result*i
    return result

result1=add_mul('add',2,3)
print(result1)
print('-'*20)
result2=add_mul('mul',2,3)
print(result2)

