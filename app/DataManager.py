
import os
import json
from TimeManager import tm, MyTime

class DataManager :
    def __init__(self) :
        self.__user = os.getcwd() + '\\static\\user\\'
        self.__menu = os.getcwd() + '\\static\\menu\\'

    def addUser(self, user_key) :
        self.setUserTime(user_key, tm.mainTime)

    def removeUser(self, user_key) :
        userPath = self.__userPath(user_key)
        if os.path.exists(userPath) :
            os.remove(userPath)

    def getUserTime(self, user_key) :
        userPath = self.__userPath(user_key)
        if not os.path.exists(userPath) :
            self.addUser(user_key)
            return tm.mainTime
        with open(userPath, 'r') as f :
            return MyTime(int(f.read()))
    
    def setUserTime(self, user_key, myTime) :
        userPath = self.__userPath(user_key)
        with open(userPath, 'w') as f :
            f.write(str(myTime.sec))

    def __userPath(self, user_key) :
        return self.__user + user_key + '.txt'

    def __menuPath(self, timeStruct) :
        return self.__menu + str(timeStruct.st[0]) + '.' + timeStruct.toString() + '.json'

    def getMenu(self, timeStruct) :
        menuPath = self.__menuPath(timeStruct)
        if not os.path.exists(menuPath) :
            return False
        with open(menuPath, 'r') as f :
            return json.loads(f.read())

    def saveMenu(self, meal) :
        menuPath = self.__menuPath(tm.mainTime)
        with open(menuPath, 'w') as f :
            f.write(json.dumps(meal))

dm = DataManager()