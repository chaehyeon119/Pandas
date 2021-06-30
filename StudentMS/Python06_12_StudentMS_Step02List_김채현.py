#Python06_12_StudentMS_Step02List_김채현

menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']

print('-'*80)
#--------------------------------
# 1문제] dic에 idList를 key값으로 하고
# scoreList를 Value값으로 할당.
#** dic['key값']=Value
#--------------------------------
#1문제 답:

for i in range(len(idList)):
	dic[idList[i]]=scoreList[i]

# print(dic) #해보면 확인할 수 있음

itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

print('-'*15)

print('학생관리시스템v01')

print('-'*80)
for i in range(len(menu)):
	print(menu[i], end='')
print()#아래줄로 가세요
print('-'*80)
while True:
	n=int(input('번호 입력:'))
	if n<3:
		print(menu[n-1],'Algorithm Chk')
#---------------------------------------
# 2문제] 3번(학생목록)을 선택한 경우 dic의 값을 출력
#----------------------------------------
	elif n==3:
		print('학생목록')
		print()
	elif n==9:
		print(menu[4])
		break
	else:
		print('올바르게 입력하세요.')


	


'''

dic = {}
deleteIDList = []
idx = 0;
'''