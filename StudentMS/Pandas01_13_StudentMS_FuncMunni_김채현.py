# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# panPrac01_13

# init
menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ', ' 9. 메뉴종료 ']
menuChk = ['1', '2', '3', '4', '9']
itemList = ['ID', '필기점수', '실기점수', '인성점수']
MenuList = ["ID", "필기", "실기", "인성", "합계", "평균", "합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"]
scoreList = [[47, 58, 85], [12, 75, 84], [57, 75, 84], [36, 86, 87],
             [89, 67, 46], [45, 86, 46], [68, 47, 98]]
dic = {}
deleteIDList = []
n = 0

#inputData
def inputData():
    for i in range(len(idList)):  # key - value match
        dic[idList[i]] = scoreList[i]

# menuPrint
def menuGui():
    print('-' * 75)
    print("학생관리시스템v01")
    print('-' * 75)
    for i in menu:
        print("%s\t" % i, end='')
    print()
    print('-' * 75)

# printList
def printList():
    sum = 0
    kList = list(dic.keys())  # key to List

    print("{0:^60}".format("학생목록"))
    for i in MenuList:
        print("%5s\t" % i, end='')
    print()
    print('-' * 75)
    for i in kList:  # Print Score
        print("%-10s" % i, end='\t')
        for j in range(len(dic[i])):  # len(dic[i]) Value의 크기를 의미
            print("%-5d" % dic[i][j], end='\t')
            sum += dic[i][j]
        print("%-5d%  -5.1f" % (sum, (sum / len(dic[i]))), end='\t')
        if 60 <= (sum / len(dic[i])) <= 100:
            print("%-10s" % "합격")
        else:
            print("%-10s" % "불합격")
        sum = 0
# InputChk
def inputChk():
    # Input
    n = input("{0:^40}".format('번호 입력 :'))
    return n

def mainPg():
    menuGui()
    n = inputChk()
    if n in menuChk:
        if n == '1':
            delID()
        elif n == '2':
            signIn()
        elif n == '3':
            printList()
        elif n == '4':
            successStu()
        elif n == '9':
            print("{0:^60}".format("종료합니다."))
            return 0
    else:  # 예외처리
        if n == '':
            print("{0:^60}".format("CHECK"))
        else:
            print("{0:^60}".format("잘못된 입력"))
            
def delID():
    print("{0:^60}".format("1. 탈퇴학생 Algorithm Check"))

def signIn():
    print("{0:^60}".format("2. 추가등록 Algorithm Check"))

def successStu():
    print("{0:^60}".format("4. 합격생목록 Algorithm Check"))



inputData()
if __name__ == '__main__':
    # run
    while True:
        mainPg()


# %%



