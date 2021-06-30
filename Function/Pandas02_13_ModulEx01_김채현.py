#Pandas02_14_RandomEx01_김채현
import random

for i in range(5): #i=0,1,2,3,4
	print('%f' %random.random(), end='')
#random.random : 실수 가져올때
print('\n','-'*50,'\n')

for i in range(5):
	print('%d'%random.randint(1,3),end='')
#randint : 범위 !1,3) 1,2,3
print('\n','-'*50,'\n')

for i in range(5):
	print('%d'%random.randint(1,45),end='')
	print()
