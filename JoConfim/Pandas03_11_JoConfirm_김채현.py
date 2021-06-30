#Pandas03_11_JoConfirm_김채현

'''
조건]
- 4인 이상 len() 인원수 반환
- 5명 -> 1~5
- 중복 없이 반환.
- 중복 없이 반환.
Sample Run]
보라돌이 뽀오 나나 뚜비
4      1   2    3
'''
import random

names = input('4인 이상 이름을 입력하세요. (Space 구분)').split()
#for문 안에 while문을 넣는다. 비교해서 넣을 수 있게 하라
b=[]
if len(names) >= 4:
	print(' '.join(names), '입력되었습니다.')
	for i in range(len(names)):
		print('%d'%random.randint(1,len(names)), end='  ')
else:
	print('명 수를 확인하세요 (4인이상))')



# if len(names) >= 4:
#     print(' '.join(names), "입력되었습니다.")
# else:
#     print('명 수를 확인하세요 (4인이상))')
