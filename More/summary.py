#1) [표현식 for 항목 in 반복 가능 객체 if 조건]
result=[x*y for x in range(2,10)
	for y in range(1,10)]
print(result)


#2) 정렬
#왼쪽 정렬
print('{0:<10}'.format('hi'))
#가운데 정렬
print('{0:^10}'.format('hi'))
#오른쪽 정렬
print('{0:>10}'.format('hi'))


#3)문자열 삽입(join)
print(','.join('abcd')) #a,b,c,d

#4) 왼쪽 공백 지우기(lstrip)
a='  hi'
print(a.lstrip())

#5) 문자열 바꾸기(replace) replace(바뀌게 될 문자열, 바꿀 문자열)
b = 'you are too short'
print(b.replace('you','Your legs'))

#리스트명=[요소1, 요소2, 요소3, ''']


#pop[리스트 요소 끄집어내기]
#pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.
a=[1,2,3]
print(a.pop()) #3

#pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제한다.
b=[1,2,3]
print(b.pop(1)) #2
print(b)#[1,3]

#리스트 확장(extend)
#extend(x)에서 x에는 리스트만 올 수 있으며 원래의 a리스트에 x리스트를 더하게 된다.
a=[1,2,3]
a.extend([4,5])
print(a) #[1,2,3,4,5]
b=[6,7]
a.extend(b)
print(a) #[1,2,3,4,5,6,7]


'''
튜플
- 리스트는 []로 둘러싸지만 튜플은 ()으로 둘러싼다.
- 리스트는 그 값의 생성,삭제,수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
- 프로그램이 실행되는 동안 그 값이 항상 변하지 않기를 바란다거나 값이 바뀔까 걱정하고 싶지 않다면
튜플을 사용해야한다. 이와는 반대로 수시로 그 값을 변화시켜야 할 경우는 리스트를 사용해야 한다.
'''
t2=(1,) #단지 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다.

'''
딕셔너리
- 딕셔너리는 리스트나 튜플처럼 순차적으로 해당 요솟값을 구하지 않고
Key를 통해 Value를 얻는다. 이것이 바로 딕셔너리의 가장 큰 특징이다.
basball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 모두 검색하는 것이 아니라
baseball이라는 단어가 있는 곳만 펼쳐 보는 것이다.

기본 딕셔너리의 모습
{Key1:Value1, Key2:Value2, Key3:Value3, ...}

딕셔너리의 예
dic={'name':'pey','phone':'0119993323','birth':'1118'}

다음 예처럼 Value에 리스트도 넣을 수 있다.
a={'a':[1,2,3]}
'''
#딕셔너리 쌍 추가하기
a={1:'a'}
a[2]='b'
print(a) # {1:'a',2:'b'}
a['name']='pey'
print(a) # {1:'a',2:'b', 'name','pey'}

#딕셔너리 요소 삭제하기
a={1:'a'}
a[2]='b'
del a[1] #key가 1인 key:value 쌍 삭제
print(a) #{2:'b'}

#딕셔너리 활용
dic={'name':'pey', 'phone':'0119993323','birth':'1118'}
print(dic['name']) #pey
print(dic['phone']) #0119993323
print(dic['birth']) #1118

#딕셔너리 만들 때 주의 사항
'''
Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시됨.
동일한 key가 존재할 경우 앞에 있는 것이 무시 됨.
'''
a={1:'a',1:'b'}
print(a)#{1:'b'}


#주의해야할 사항
'''
Key에 리스트X, 튜플O
딕셔너리의 key로 쓸 수 있냐 없냐는 key가 변하는 값인지 아닌지에 달림.
리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없다. 
'''

#key 리스트 만들기(keys)
a={'name':'pey','phone':'0119993323','birth':'1118'}
print(a.keys()) #dict_keys(['name', 'phone', 'birth'])
for k in a.keys():
	print(k)
#name
#phone
#birth

#dict_keys 객체를 리스트로 변환하려면
list(a.keys())
print(list(a.keys())) #['name', 'phone', 'birth']

#Key, Value 쌍 얻기(items)
print(a.items()) #dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

#Key:Value 쌍 모두 지우기(clear)
print(a.clear()) # none

#key로 value 얻기(get)
a={'name':'pey','phone':'0119993323','birth':'1118'}
print(a.get('name')) #pey
#get['name']은 a['name']과 동일 결과값을 받을 수 있음


#디폴트값
'''
딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해 둔 디폴트 값을
대신 가져오게 하고 싶을 때에는 get(x,'디폴트값')을 사용하면 됨
'''
print(a.get('foo','bar')) #bar

#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a={'name':'pey','phone':'0119993323','birth':'1118'}
print('name' in a) #True


#집합 자료형의 특징
s2=set('hello')
print(s2) #{'o', 'l', 'h', 'e'}

'''
1. 중복을 허용하지 않는다.
2. 순서가 없다.
'''
#set 자료형 리스트나 튜플로 전환하기
s1=set([1,2,3])
l1=list(s1)
print(l1) #[1, 2, 3]
t1=tuple(s1)
print(t1)#(1, 2, 3)

#교집합, 합집합,차집합 구하기
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#교집합
print(s1&s2)#{4,5,6}
#s1.intersection(s2)와도 같은 결과

#합집합
print(s1|s2) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
#s1.union(s2)와도 같은 결과

#차집합
print(s1-s2)#{1, 2, 3}
#s1.difference(s2)와 같은 값

#값 1개 추가하기(add)
s1=set([1,2,3])
s1.add(4)
print(s1)#{1,2,3,4}

#값 여러 개 추가하기(update)
s1=set([1,2,3])
s1.update([4,5,6])
print(s1)#{1, 2, 3, 4, 5, 6}

#특정 값 제거하기(remove)
s1=set([1,2,3])
s1.remove(2)
print(s1)#{1,3}


#1) [표현식 for 항목 in 반복 가능 객체 if 조건]
result=[x*y for x in range(2,10)
	for y in range(1,10)]
print(result)


#2) 정렬
#왼쪽 정렬
print('{0:<10}'.format('hi'))
#가운데 정렬
print('{0:^10}'.format('hi'))
#오른쪽 정렬
print('{0:>10}'.format('hi'))


#3)문자열 삽입(join)
print(','.join('abcd')) #a,b,c,d

#4) 왼쪽 공백 지우기(lstrip)
a='  hi'
print(a.lstrip())

#5) 문자열 바꾸기(replace) replace(바뀌게 될 문자열, 바꿀 문자열)
b = 'you are too short'
print(b.replace('you','Your legs'))


# 시계 문제
H=int(n[0]) #'='의 의미는 오른쪽 값을 왼쪽 변수에 대입(저장)
M=int(n[1]) #'='의 의미는 오른쪽 값을 왼쪽 변수에 대입(저장)


#정수로 입력을 받으면 split을 못씀. 문자로 받고 쪼갠 다음에 정수로 바꿔야 함.
while True:
	n=input("시간을 입력하시오. (Space)를 기준으로 '시'와 '분' 인식  ").split(' ')
	H=int(n[0]) #오른쪽 값을 왼쪽 변수에 대입(저장)
	M=int(n[1]) #오른쪽 값을 왼쪽 변수에 대입(저장)


#가운데 배열로 포맷형식 활용하기
print('{0:^50}'.format('지금 시간은 %d : %d' %(H, M)))
#에러났던 이유: 괄호 하나 덜 넣음

print('{0:^50}'.format('지금 시간은 {} : {}'.format(H, M)))