'''
# mod1.py

함수 : 재사용

모듈 : 함수들의 모임 ----> 결국은 재사용하기 위해
import 모듈명

'''



def sum(a, b):
    return a + b

def safe_sum(a, b): 
    if type(a) != type(b): 
        print("더할수 있는 것이 아닙니다.")
        return 
    else: 
        result = sum(a, b) 
    return result



