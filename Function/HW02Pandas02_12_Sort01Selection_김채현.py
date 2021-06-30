'''
**Selection sort
1. 오름차순
	- 숫자: 작은수 -> 큰수
	- 영문: A->Z
	- 한글: ㄱ->ㅎ

2. 내림차순
	- 숫자: 큰수 -> 작은수
	- 영문: Z->A
	- 한글: ㅎ->ㄱ
'''

#HW02Pandas02_12_Sort01Selection_김채현



sortNum = [2,5,6,1,2,8,33,77,12]

for i in range(len(sortNum)-1):
	for j in range(i+1,len(sortNum)):
		if (sortNum[i]>sortNum[j]):
			Temp=sortNum[i] #교환 Algorithm)
			sortNum[i]=sortNum[j]
			sortNum[j]=Temp
print(sortNum)

print('%d회차 :'%(i+1), end= ' ')
for k in sortNum:
	print(k, end= ' ')
print()

