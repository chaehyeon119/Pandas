
#HW02Pandas03_04_ClassEx04_김채현

'''
하나의 클래스에 똑같은 이름의 메소드가 2개 이상있는 것을
오버로드라고 한다.
오버로드
1. 같은 클래스의 같은 메소드가 2개 이상
2. 매개변수의 개수로 구분한다
'''

class FourCal:
	def __init__(self): #1) 매개변수 없음
		pass #블럭 아래 무엇이든 써야하니까 아무것도 없으면 pass 써줘야함 안 쓰면 에러

	def __init__(self,first,second):#2) 매개변수 2개
		self.first=first
		self.second=second
#------(오버로드/FourCal 클래스에 같은 이름의 메소드가 2개이기 때문)----------------
#a=FourCal(4,2) 생성자가 2개 있으니까 2)에 넣어짐 아무것도 없었으면 1)에 넣어질 것임

	def sum(self):
		result=self.first+self.second
		return result
	def sub(self):
		result=self.first-self.second
		return result
	
	def mul(self):
		result=self.first*self.second
		return result

	def div(self):
		result=self.first/self.second
		return result
#a=FourCal()
#a.setdata(4,2)

a=FourCal(4,2)


Callist = ['+','-','*','/']
Sollist = [a.sum(),a.sub(),a.mul(),a.div()]



for i in range(len(Callist)):
	print(a.first,Callist[i],a.second,'=',Sollist[i])