
#HW02Pandas03_06_ClassEx06_김채현


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

class SafeFourCal(FourCal):
	def div(self):#현재 메소드 우선
		if self.second==0:
			return 0
		else:
			return super().div()#super(상위클래스) 상위클래스의 div를 구현하라
a=SafeFourCal(4,0) #상속


print(a.first,'+',a.second,'=',a.sum())#4+0=4
print(a.first,'-',a.second,'=',a.sub())#4-0=4
print(a.first,'*',a.second,'=',a.mul())#4*0=0
print(a.first,'/',a.second,'=',a.div())#4/0=0


'''
Callist = ['+','-','*','/']
Sollist = [a.sum(),a.sub(),a.mul(),a.div()]
for i in range(len(Callist)):
	print(a.first,Callist[i],a.second,'=',Sollist[i])
'''
