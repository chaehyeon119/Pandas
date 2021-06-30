#HW02Pandas02_15_joConfirmStep02_김채현
'''
조건]
- 4인 이상 len() 인원수 반환
- 만약에 5명 -> 1~5
- 중복 없이 반환.

Sample Run]
보라돌이 뽀오 나나 뚜비
4      1   2    3

'''
for idx in range(5):
	list01=[4,4
	for idx in range(5):
		앞쪽을 비교하는 알고리즘 짜기
		앞쪽비교 idx-1
'''
'''
#중복을 해결하는 답안을 짜라 

import sys
import random

while True:
	a=[]

	a=input('4인 이상의 이름을 입력하세요.(종료 :0)').split()
	if 'O' in a:
		exit()

	if len(a)<4:
		print('^\t명수를 확인하세요.')
		continue
	else:
		while True:
			num=random.randint(1,len(a))
			if num no im b:
				b.append(num)
			else:
				continue
			
			if len(b)==len(a):
				break

		for i in a:
			print(i, end='')
		print('이고')
		for i in b:
			print(i,end='')
		print('입니다.')
	