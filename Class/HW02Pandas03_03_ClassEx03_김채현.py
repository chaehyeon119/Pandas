#HW02Pandas03_03_ClassEx03_김채현

class FourCal:
	def setdata(self,first,second):
		self.first=first
		self.second=second
	
	def sum(self):
		result=self.first+self.second
		return result
	
	def sub(self):
		result=self.first-self.second
		return result

	def mul(self):
		result=self.first * self.second
		return result
	
	def div(self):
		result=self.first / self.second
		return result

a=FourCal()
a.setdata(4,2)

#식 써줘야함
#다른 사람들 코드보면서 이해하기
