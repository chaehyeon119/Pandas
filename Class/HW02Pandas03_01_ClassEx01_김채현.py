#HW02Pandas03_01_ClassEx01_김채현
'''
##클래스
틀, 구조
함수+속성
-거푸집:
 ->객체: 클래스로부터 생성
생성자: 함수, 클래스 이름과 동일한 함수, 주로 초기화

class는 소괄호는 없는데
가지고 올때는 소괄호 붙여야함 
ex)
clss Fourcal:~~
a=Fourcal()

##클래스 사용
- 객체 생성 후 사용
- 객체.속성 or 객체.함수...'

self는 판다스의 개념 
self는 현재 객체(Fourcal)을 의미함.

풀빵 틀은 클래스
거기서 나온 풀빵들은 객체
'''

class Fourcal:
	def setdata(self, first, second):
		self.first=first
		self.second=second

a= Fourcal() #이때, a가 객체
a.setdata(4,2) #self가 a를 가리킴 만약, b.setdata이면 self는 b를 가리킴

print(a.first) #4
print(a.second) #2
print(type(a)) #<class ' __main__.Fourcal'>