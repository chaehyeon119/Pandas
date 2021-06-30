#Pandas02_02_FunEx7_김채현

#디폴트값 man=True
def say_myself(name,old,man=True):
	print('나의 이름은 %s입니다.'%name)
	print('나이는 %d입니다.' %old)
	if man:
		print('남자입니다.')
	else:
		print('여자입니다.')


say_myself('소나무',27,)  #왜 소나무가 남자로 뜨는가?
print('-'*20)
say_myself('오렌지',25,False) #다를 때만 수정해라
print('-'*20)