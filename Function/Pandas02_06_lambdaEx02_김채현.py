#Pandas02_06_lambdaEx02_김채현

#함수 안에서 lambda가 있음

#lambda 활용법 lambda 매개변수: 표현식

x=lambda a:a+10
print(x(5)) #15

x=lambda a,b:a*b
print(x(5,6)) #30

def myfunc(n):
	return lambda a:a*n

mydoubler=myfunc(2)
print(mydoubler(11)) #22 #11*2


mytripler=myfunc(3)
print(mytripler(11)) #33
