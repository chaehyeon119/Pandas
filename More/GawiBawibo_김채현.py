#GawiBawibo_김채현

import random as rd

menuChk = ['1','2','3','4','9']
computer= 0
List=['가위', '바위', '보']
User=0
Win=[0,0]


print()
print()
while True:
	print('1. 가위', '2. 바위','3. 보', '4. 횟수입력', '9. 종료')
	n=int(input("      번호를 선택하세요."))
	computer=rd.randint(0,2)
	print('\n', '-' * 50, '\n')
	print('Com :', List[computer], '/User :', List[n-1])
	if computer==n-1:
		print('게임에서 비겼습니다.')
	elif computer==0 and n-1==1 or computer==1 and n-1==2 or computer==2 and n-1==0:
		print('You Win! 당신이 이겼습니다!')
		Win[1]=Win[1]+1
	elif computer==1 and n-1==0 or computer==2 and n-1==1 or computer==0 and n-1==2:
		print('게임에서 졌습니다.')
		Win[0]=Win[0]+1
		print('=> 현재 스코어', Win[0], ':',Win[1], '(컴퓨터 : 당신)입니다.')
	else:
		print('종료합니다.')
		exit()
		

	print( )


	#elif n==9:
	#	print('종료합니다.')
		#break