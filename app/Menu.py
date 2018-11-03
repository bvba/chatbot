
from bs4 import BeautifulSoup
from Src import src 
from TimeManager import tm, MyTime # tm == TimeManager
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
        print('Menu update')
        self.__init__()

    # 아침 or 점심 or 저녁을 인자로 넘기면 해당하는 메뉴 반환
    def getMeal(self, content, myTime = tm.mainTime) :
        return '[' + content + '] - ' +	\
               str(myTime.st[1]) + '.' + str(myTime.st[2]) + '\n' + \
               self.__meal[myTime][content]

    def getTodayMeal(self) :
        ret = ''
        for content in src.mealTime :
            ret += getMeal(content)
        return ret

    def __setUrl(self, myTime = tm.mainTime) :
        self.__url = 'https://coop.koreatech.ac.kr:45578/dining/menu.php' + \
                     '?sday=' + str(myTime.sec)

    # 메뉴 파싱
    def __parsing(self) :
        for day in range(6) :
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

menu = Menu()
