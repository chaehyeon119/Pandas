#Pandas03_09_StuMS_FunMunni_김채현

#Python06_12_StudentMS_Step02_김채현

menu = [' 1. 회원가입 ', ' 2. 로그인 ', ' 3. 회원목록 ', '9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']

print('='*30,'메뉴선택','='*30)
print()

#print('%s %s %s %s %15s'%(menu[0],menu[1],menu[2],menu[3],menu[4]))
for i in range(len(menu)):
	print(menu[i], end='')
print()#아래줄로 가세요
print('='*70)
while True:
	n=int(input('번호 입력:'))
	if n==4:
		print('SignUP')
	elif n==9:
		print(menu[4])
		break
	else:
		print('올바르게 입력하세요.')


	'''
	if n=='1':
		print('{0:^30}'.format('1. 회원가입 Algorithm Chk'))
	elif n=='2':
		print('{0:^30}'.format('2. 로그인 Algorithm Chk'))
	elif n==3:
		print('{0:^30}'.format('3. 회원목록 Algorithm Chk'))
	elif n==9:
		print('\t', '메뉴종료')
		break
	else:
		print('메뉴의 번호를 선택해주세요.')
	'''	