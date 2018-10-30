
import time


class TimeManager() :
    def __init__(self) :
        ltime = list(time.localtime())
        ltime[3:6] = [0, 0, 0] # hour, min, second = 0, 0, 0
        ltime = time.struct_time(ltime)

        self.mainTime = MyTime(ltime)
        del ltime

    def update(self) :
        ltime = list(time.localtime())
        currTime = str(ltime[3]) + str(ltime[4])
        if currTime >= '1830' :
            self.mainTime = MyTime(self.mainTime.sec + 86400)
            return True
        elif list(self.mainTime.st)[:3] != ltime[:3] :
            self.__init__()
            return True
        return False
        

class MyTime() :
    def __init__(self, st = None, sec = None) :
        '''
        st == time.struct_time
        sec == time.mktime(st)
        '''
        if st != None and sec != None :
            print('MyTime init error')
            exit()
        elif type(st) == time.struct_time :
            self.st = st
            self.sec = int(time.mktime(st))
        elif type(sec) == int :
            self.sec = sec
            self.st = time.localtime(sec)
        else :
            self.st = time.localtime(0)
            self.sec = 0 # time.mktime(st)


tm = TimeManager()
