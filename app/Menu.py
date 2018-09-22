
import time

class Menu :
    def __init__(self) :
        self.__date = list(time.localtime())[:3]
        self.__keyboard = dict()
        self.__menuList = dict()
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
        self.__keyboard = {
            'type' : 'buttons',
            'buttons' : ['한식', '일품', '전골 or 뚝배기', '양식', '능수관']
        }
        self.__menuList['korean'] = {'text' : 'korean'}
        self.__menuList['onedish'] = {'text' : 'onedish'}
        self.__menuList['special'] = {'text' : 'special'}
        self.__menuList['western'] = {'text' : 'western'}
        self.__menuList['faculty'] = {'text' : 'faculty'}
        
menu = Menu()
