#Python06_12_StudentMS_Step02_김채현

menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']

print('-'*80)

print('학생관리시스템v01')

print('-'*80)
#print('%s %s %s %s %15s'%(menu[0],menu[1],menu[2],menu[3],menu[4]))
for i in range(len(menu)):
	print(menu[i], end='')
print()#아래줄로 가세요
print('-'*80)
while True:
	n=int(input('번호 입력:'))
	if n<=4:
		print(menu[n-1],'Algorithm Chk')
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


'''

itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;
'''