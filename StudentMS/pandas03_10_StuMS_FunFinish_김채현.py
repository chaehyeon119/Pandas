menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ', ' 9. 메뉴종료 ']
menuChk = ['1', '2', '3', '4', '9']
itemList = ['ID', '필기점수', '실기점수', '인성점수']
MenuList = ["ID", "필기", "실기", "인성", "합계", "평균", "합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"]
scoreList = [[47, 58, 85], [12, 75, 84], [57, 75, 84], [36, 86, 87],
             [89, 67, 46], [45, 86, 46], [68, 47, 98]]
dic = {}
deleteIDList = []

# 학생 수를 체크
def menuGui(number):
    number = number+ 1
    return number

# 딕셔너리에 전역으로 값 할당, main 컴파일 이전에 사용
def inputData():
	for i in range(len(idList)):
		dic[idList[i]] = scoreList[i]

# menuPrint
def menuGui():  # 메뉴를 출력하는 함수
    print('-' * 75)
    print("학생관리시스템v01")
    print('-' * 75)
    for i in menu:
        print("%s\t" % i, end='')
    print()
    print('-' * 75)

# printList
def printList():  # dictinoary 생성
    sum = 0
    kList = list(dic.keys())  # key to List,
    print("{0:^60}".format("학생목록"))
    for i in MenuList:
        print("%5s\t" % i, end='')
    print()
    print('-' * 75)
    for i in kList:  # Print Score, kList 쓰지 않고, idList 사용 가능
        print("%-10s" % i, end='\t')
        for j in range(len(dic[i])):  # len(dic[i]) Value의 크기를 의미
            print("%-5d" % dic[i][j], end='\t')
            sum = sum + dic[i][j]
        print("%-5d%  -5.1f" % (sum, (sum / len(dic[i]))), end='\t')
        if 60 <= (sum / len(dic[i])) <= 100:
            print("%-10s" % "합격")
        else:
            print("%-10s" % "불합격")
        sum = 0


def mainPg():
    while True:
        menuGui()
        # Input
        n = input("{0:^40}".format('번호 입력 :'))
        if n in menuChk:
            if n == '1':
                delID()
            elif n == '2':
                signIn()
            elif n == '3':
                printList()
            elif n == '4':
                passStu()
            elif n == '9':
                print("{0:^60}".format("종료합니다."))
                return 0
        else:  # 예외처리
               print("{0:^60}".format("잘못된 입력"))



def delID():
    print("{0:^60}".format("탈퇴학생"))
    dID = input("{0:^40}".format("탈퇴할 학생 ID : "))
    if dID in idList:  # id제거
        del dic[dID]
        deleteIDList.append(dID)
        print("{0:^60}".format("%s 학생이 탈퇴하였습니다." % dID))
    else:
        print("{0:^60}".format("해당 ID가 없습니다."))


def signIn():
    temp = [0 for i in range(len(itemList) - 1)]
    print("{0:^60}".format("추가등록"))
    addID = input("{0:^40}".format("추가등록 할 학생 ID : "))
    if addID not in idList:
        for i in range(1, len(temp) + 1):
            temp[i - 1] = int(input('%s : ' % itemList[i]))
        dic[addID] = temp
    else:
        if addID in deleteIDList:
            print("탈퇴 회원입니다. 가입불가!")
        else:
            print("중복된 회원입니다. 다시 입력해주세요.")
            signIn()


def passStu():
    print("{0:^60}".format("4. 합격생목록 Algorithm Check"))



inputData()
while True:
    mainPg()
