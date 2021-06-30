#Pandas02_04_FunEx9_김채현
#함수 안에서 함수 밖의 변수를 변경하는 방법

#1.return 사용하기 return a 6번라인에 있는 변수 변경된 값(2) 10번에서 a를 재할당함
a=1
def vartest(a):
	a=a+1
	return a


a= vartest(a)
print(a) #2
print('-'*20)

#2. global 명령어 사용하기
#global 명령어 : 함수 안에서 함수 밖의 변수를 직접 사용할 때 사용. 권장x
#외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다.

a=1
def vartest():
	global a
	a=a+1

vartest()
print(a) #2