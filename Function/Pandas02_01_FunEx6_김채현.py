#Pandas02_01_FunEx6_김채현

#returen문을 2번 사용하면,
#두 번째 return문인 returen a*b는 실행되지 않았다

def add_and_mul(a,b):
	return a+b #7에서 이미 돌아갔으므로
	return a*b #8은 실행되지 않음

result=add_and_mul(2,3)
print(result)   #5
print('-'*10)


#[return]의 또 다른 쓰임새
#return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.
#원하지 않는 값을 받았으면 return 시킴
#바보 오면 return시키고 진행시키지 않음. 아니면 프린트

def say_nick(nick):
	if nick=='바보':
		return
	print('나의 별명은 %s입니다.'%nick) #나의 별명은 야호입니다.

#1)
say_nick('야호')
say_nick('바보')
### 1), 2) 둘 다 같은 거임
#2)
result=say_nick('야호')
result=say_nick('바보')
print('-'*10)
