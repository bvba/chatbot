
import os
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
        if not os.path.exists(userPaht) :
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

    def getMenu(self, timeStruct, content) :
        None

    def saveMenu(self, meal) :
        None

dm = DataManager()