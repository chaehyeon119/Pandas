#Pandas02_16_ModuleEx02_김채현

from mod1 import sum,safe_sum
print(sum(3,4))
print(safe_sum(3,5)) #?


'''
#def safe_sum(a,b):
	if type(a)!=type(b):
		print('더할수 있는 것이 아닙니다.')
		return
	else:
		result=sum(a,b)
	return result
	'''