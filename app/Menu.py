
from bs4 import BeautifulSoup
from Src import src 
from TimeManager import tm, MyTime # tm == TimeManager
from DataManager import dm
from multiprocessing import Pool
import time
import urllib.request


class Menu :
    def __init__(self) :
        # 식단 정보
        self.__meal = dict()

        # parsing url
        self.__setUrl()

        self.__parsing()

    def update(self) :
        self.__init__()

    def getMealSize(self) :
        return len(self.__meal)

    # 아침 or 점심 or 저녁을 인자로 넘기면 해당하는 메뉴 반환
    def getMeal(self, content, myTime = tm.mainTime) :
        return '[' + content + '] - ' +	myTime.toString() + '\n' + \
                (self.__meal[myTime][content] if myTime >= tm.mainTime else dm.getMenu(myTime)[content])

    def __setUrl(self, myTime = tm.mainTime) :
        self.__url = 'https://coop.koreatech.ac.kr:45578/dining/menu.php' + \
                     '?sday=' + str(myTime.sec)

    # 메뉴 파싱
    def __parsing(self) :
        print('Menu.py - ' + __name__)
        startTime = time.time()

        # mon, tue, wed, thu : ~sun 그 주 일요일까지 메뉴 확인 가능
        # fri, sat, sun : ~ sun ~ sun 그 다음 주 일요일까지 메뉴 확인 가능
        dayRange = 7 - tm.mainTime.st[6]
        if tm.mainTime.st[6] > 3 :
            dayRange += 7

        
        for day in range(dayRange) :
            myTime = MyTime(tm.mainTime.sec + day * 86400)
            self.__setUrl(myTime)

            with urllib.request.urlopen(self.__url) as fs :
                soup = BeautifulSoup(fs.read()
                                     .decode('euc-kr')
                                     .replace('timeo', 'time')
                                     .replace('listo', 'list')
                                     .replace('\r', '')
                                     .replace('\t', '')
                                     .replace('kcal', 'kcal\n')
                                     , 'html.parser')
                items = soup.find_all('td', {'class' : 'menu-list'})

            self.__meal[myTime] = dict()
            # 아침 점심 저녁
            for i in range(3) :
                tmpData = ''
                # 한식, 일품, 특식, 양식, 능수관
                for j in range(5) :
                    txt = items[i * 8 + j].get_text()
                    if txt == '\n\xa0\n' : continue
                    tmpData += ('# ' + src.mealType[j] + txt + '─' * 12 + '\n')
                self.__meal[myTime][src.mealTime[i]] = tmpData[:-2]
        
        # 메뉴 변동 가능성이 있으므로 오늘 메뉴만 저장하고
        # 이후 날짜의 메뉴는 저장하지 않는다.
        dm.saveMenu(self.__meal[tm.mainTime])

        endTime = time.time()
        print('Menu.py - parsing time : ' + str(endTime - startTime))

    

menu = Menu()
