
from parsing import meal
import time

class Menu :
    def __init__(self) :
        self.__date = list(time.localtime())[:3]
        self.__keyboard = dict()
        self.__meal = []
        self.__update()

    def getKeyboard(self) :
        self.__dateChk()
        return self.__keyboard

    def getMenu(self, menu) :
        __dateChk()
        return self.munuList[menu]

    def __dateChk(self) :
        if self.__date != list(time.localtime())[:3] :
            self.__update()

    def __update(self) :
        print('update')
        self.__keyboard = {
            'type' : 'buttons',
            'buttons' : ['한식', '일품', '전골 or 뚝배기', '양식', '능수관']
        }
        self.__meal = meal
        
menu = Menu()
