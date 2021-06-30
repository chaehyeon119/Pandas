menu=['1.탈퇴학생', '2.추가등록','3.학생목록','4.합격생목록','9.메뉴종료']
menuChk=['1','2','3','4','9']
c=['ID','필기점수','실기점수','인성점수']
MenuList=['ID','필기','실기','인성','합계','평균','합격유무']

idList=['Orange','Red','Yellow','Green','Blue','Navy','Purple']

scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic={}
deleteIDList=[]
idx=0;

def inputData():
	for i in range(0, len(idList)):
