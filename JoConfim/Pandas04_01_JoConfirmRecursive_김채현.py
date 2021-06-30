#Pandas04_01_JoConfirmRecursive_김채현
#재귀함수(recursive)

import random
lst= []

def recursive(m):
	if(chk==len(lst)):
		return
	
	for i in range(m):
		num=random.randint(1,len(name))
		if num not in lst:
			lst.append(num)
		else:
			recursive(chk-len(lst))

while True:
	name=input('4인 이상의 이름을 입력하세요.(Space Bar로 구분한다.)').split()
	if len(name)>=4:
		for i in name:
			print(i, end=' ')
		print('')
		
		
		chk=len(name)
		

		lst=[]#이게 왜 2번이나 들어가는 것일까

		recursive(chk)
		print(lst)